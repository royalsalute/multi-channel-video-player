import os

import cv2

import datetime
import threading
import numpy as np
import pandas as pd
import time

from util import image_resize, get_qimage, FPS, NUM_CHANNEL
from PyQt5 import QtCore, QtGui, QtWidgets


num = 0


class Channel(QtWidgets.QLabel):
    capture = cv2.VideoCapture()

    cur_video = None
    df = pd.DataFrame()
    frame = None
    frame_pos = 0
    entry = None
    i_poses = None
    tracks = {}

    def __init__(self, parent, channel_no, *args, **kwargs):
        super(Channel, self).__init__(parent)
        self.channel_no = channel_no

    def load_metadata(self, df, day_start):
        self.date = day_start
        self.df = df[df['channel'] == self.channel_no]

        # Build tracks for channel
        self.tracks = {}
        for i in self.df.index:
            row = self.df.loc[i]
            self.tracks[i] = (max((row['start_time'] - day_start).total_seconds(), 0), min((row['end_time'] - day_start).total_seconds(), 3600 * 24 - 1))

    def get_track_by_timestamp(self, msecs):
        filtered_tracks = {key: value for (key, value) in self.tracks.items() if (value[0] * 1000 <= msecs) and (value[1] * 1000 >= msecs)}
        if len(filtered_tracks) > 0:
            return list(filtered_tracks.keys())[0]
        else:
            return -1

    def get_step_frame(self, msecs, delta):
        frame = None
        if self.capture.isOpened():
            # calculate frame position from milliseconds
            msecs_per_frame = 1000 / FPS
            s_time_msecs = (self.entry['start_time'] - self.date).total_seconds() * 1000
            frame_pos = int((msecs - s_time_msecs) / msecs_per_frame)

            if (delta >= 1) and (delta <= 16):
                ret = True
                if delta > 1:
                    # skip delta-1 frames (for 2x, 4x, 8x, 16x)
                    for i in range(delta - 1):
                        ret = self.capture.grab()
                        if not ret:
                            break
                if ret:
                    ret, frame = self.capture.read()
            elif delta > 16:
                # t = time.perf_counter()
                if not self.change_frame_pos(frame_pos + delta):
                    frame = None
                else:
                    ret, frame = self.capture.read()
                # elapsed = (time.perf_counter() - t) * 1000
                # print('Seek: %1.2fms' % elapsed)
            elif delta < 0:
                if not self.change_frame_pos(frame_pos + delta):
                    frame = None
                else:
                    ret, frame = self.capture.read()

            if frame is None:
                self.capture.release()

        if frame is None:
            if self.find_matching_video(msecs):
                ret, frame = self.capture.read()

        self.frame = frame

    def step(self, offset_msecs, delta):
        self.get_step_frame(offset_msecs, delta)

    def seek_to(self, msecs):
        if self.capture.isOpened():
            msecs_per_frame = 1000 / FPS
            s_time_msecs = (self.entry['start_time'] - self.date).total_seconds() * 1000
            frame_pos = int((msecs - s_time_msecs) / msecs_per_frame)
            if self.change_frame_pos(frame_pos):
                ret, frame = self.capture.read()
                if ret:
                    self.frame = frame
                    self.frame_pos = int(self.capture.get(cv2.CAP_PROP_POS_FRAMES))
                    return

        if self.find_matching_video(msecs):
            ret, frame = self.capture.read()
            if ret:
                self.frame = frame
                self.frame_pos = int(self.capture.get(cv2.CAP_PROP_POS_FRAMES))
                return

        else:
            self.frame = None

    def change_frame_pos(self, new_pos):
        if self.i_poses is not None:
            for i in range(len(self.i_poses) - 1):
                if (new_pos >= self.i_poses[i]) and (new_pos < self.i_poses[i + 1]):
                    ret = self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.i_poses[i] + 1)
                    if not ret:
                        return False
                    for j in range(new_pos - self.i_poses[i]):
                        ret = self.capture.grab()
                        if not ret:
                            return False
                    return True
        else:
            if self.capture.set(cv2.CAP_PROP_POS_FRAMES, new_pos):
                return True
        return False

    def find_matching_video(self, msecs):
        index = self.get_track_by_timestamp(msecs)
        if index >= 0:
            row = self.df.loc[index]
            self.entry = row
            self.capture = cv2.VideoCapture(row['path'])
            self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 20)
            cur_time = self.date + datetime.timedelta(milliseconds=msecs)
            if self.capture.isOpened():
                df_path, _ = os.path.splitext(row['path'])
                df_path = df_path + '.csv'
                i_poses_df = pd.read_csv(df_path)
                self.i_poses = i_poses_df['i-index'].tolist()

                msecs_per_frame = 1000 / FPS
                s_time_msecs = (self.entry['start_time'] - self.date).total_seconds() * 1000
                frame_pos = int((msecs - s_time_msecs) / msecs_per_frame)
                self.change_frame_pos(frame_pos)

                return True
            else:
                self.i_poses = None
        return False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        w = self.frameGeometry().width()
        h = self.frameGeometry().height()

        img = np.zeros([h, w, 3], dtype=np.uint8)
        img[:, :] = (240, 240, 240)

        if self.frame is not None:
            # frame = image_resize(self.frame, w)
            # y1 = max(0, (img.shape[0] - frame.shape[0]) // 2)
            # y2 = y1 + frame.shape[0]
            # img[y1:y2] = frame[:]

            img = cv2.resize(self.frame, (img.shape[1], img.shape[0]))

        img = cv2.rectangle(img, (0, 0), (img.shape[1] - 1, img.shape[0] - 1), (64, 64, 64), 1)
        painter.drawImage(QtCore.QPoint(0, 0), get_qimage(img))
