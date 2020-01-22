import os
import subprocess
import cv2
import datetime
import pandas as pd
import threading

from os import listdir

from PyQt5 import QtCore, QtGui, QtWidgets


extraction_running = False

class ExtractingKeyframesRunnable(QtCore.QRunnable):
    def __init__(self, data, progress):
        QtCore.QRunnable.__init__(self)
        self.data = data
        self.progress = progress

    def run(self):
        global extraction_running

        count = len(self.data)
        for i, val in enumerate(self.data):
            vname, vpath = val

            QtCore.QMetaObject.invokeMethod(self.progress, "setValue",
                QtCore.Qt.QueuedConnection, QtCore.Q_ARG(int, i))
            QtCore.QMetaObject.invokeMethod(self.progress, "setLabelText",
                QtCore.Qt.QueuedConnection, QtCore.Q_ARG(str, 'Please wait while extracting %s(%d/%d)...' % (vname, i + 1, count)))

            df_path, _ = os.path.splitext(vpath)
            df_path = df_path + '.csv'
            if os.path.exists(df_path):
                continue

            command = 'bin/ffprobe -show_entries frame=pict_type -threads 4 -of default=noprint_wrappers=1'.split()
            out = subprocess.check_output(command + [vpath]).decode()
            if extraction_running is False:
                break

            f_types = out.replace('pict_type=', '').split()
            frame_types = zip(range(len(f_types)), f_types)
            i_indexes = [x[0] for x in frame_types if x[1] == 'I']

            df = pd.DataFrame({'i-index': pd.Series(i_indexes)})
            df.to_csv(df_path, index=False)

        QtCore.QMetaObject.invokeMethod(self.progress, "setValue",
                                        QtCore.Qt.QueuedConnection, QtCore.Q_ARG(int, count))
        extraction_running = False


class VideoLoader:

    def load_directory(self, video_path, df, parent):
        global extraction_running

        mp4_files = []
        for f in listdir(video_path):
            fname, ext = os.path.splitext(os.path.join(video_path, f))
            if ext == '.mp4':
                mp4_files.append(os.path.join(video_path, f))

        info = []
        for f in mp4_files:
            cap = cv2.VideoCapture(f)
            if cap.isOpened():
                filename = os.path.basename(f)
                if df[df['filename'] == filename].shape[0] == 0:
                    fname, _ = os.path.splitext(filename)

                    fps = cap.get(cv2.CAP_PROP_FPS)
                    duration_secs = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) / fps)
                    terms = fname.split('_')
                    channel = int(terms[0][2:])
                    dt = terms[1]
                    start_time = datetime.datetime(int(dt[:4]), int(dt[4:6]), int(dt[6:8]),
                                                   int(dt[8:10]), int(dt[10:12]), int(dt[12:14]))
                    end_time = start_time + datetime.timedelta(seconds=duration_secs)

                    df = df.append({'filename': filename, 'path': f, 'channel': channel, 'start_time': start_time, 'end_time': end_time, 'duration': duration_secs, 'fps': fps},
                                   ignore_index=True)

                    info.append((filename, f))

                cap.release()

        if len(info) > 0:
            self.progress = QtWidgets.QProgressDialog('Start Extracting Keyframes...', 'Cancel', 0, len(info), parent=parent)
            self.progress.setWindowTitle("Extracting Keyframes...")
            self.progress.setWindowModality(QtCore.Qt.ApplicationModal)
            self.progress.setMinimumSize(QtCore.QSize(640, 100))
            self.progress.setMaximumSize(QtCore.QSize(640, 100))
            self.progress.setAutoClose(True)
            self.progress.setValue(0)
            self.progress.canceled.connect(self.cancelExtraction)
            self.progress.show()

            extraction_running = True
            self.doGenerate(info)

            while(extraction_running):
                cv2.waitKey(1000)

            return df, not self.progress.wasCanceled()
        else:
            return df, False

    def doGenerate(self, data):
        self.runnable = ExtractingKeyframesRunnable(data, self.progress)
        QtCore.QThreadPool.globalInstance().start(self.runnable)

    def cancelExtraction(self):
        global extraction_running
        extraction_running = False