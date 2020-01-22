# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwnd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import pandas as pd
import datetime
import os
import sys
import time

from channel import Channel
from videoloader import VideoLoader
from channelviewer import ChannelViewer
from labeledslider import LabeledSlider
from util import FPS, NUM_CHANNEL


def intersect_date(df_start_time, df_end_time, w_start_time, w_end_time):
    latest_start = max(df_start_time, w_start_time)
    earliest_end = min(df_end_time, w_end_time)
    return earliest_end > latest_start


class Ui_MainWindow(object):
    is_playing = False

    def __init__(self, csv_path=''):
        try:
            self.df_origin = pd.read_csv(csv_path, parse_dates=['start_time', 'end_time'])
        except:
            self.df_origin = pd.DataFrame(columns=['filename', 'path', 'channel', 'start_time', 'end_time', 'duration', 'fps'])
        self.df = self.df_origin

        self.labels = []
        for i in range(25):
            self.labels.append('%.2d:00' % i)

    def initChannels(self):
        self.channels = [
            self.screen1_1,
            self.screen1_2,
            self.screen1_3,
            self.screen1_4,
            self.screen1_5,
            self.screen1_6,
            self.screen1_7,
            self.screen1_8,
            self.screen1_9,
            self.screen1_10,
            self.screen1_11,
            self.screen1_12,
            self.screen1_13,
            self.screen1_14,
            self.screen1_15,
            self.screen1_16
        ]

    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.ui = self

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1700, 1053)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.screen1_1 = Channel(self.centralwidget, 1)
        self.screen1_1.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_1.setText("")
        self.screen1_1.setObjectName("screen1_1")
        self.horizontalLayout.addWidget(self.screen1_1)
        self.screen1_2 = Channel(self.centralwidget, 2)
        self.screen1_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_2.setText("")
        self.screen1_2.setObjectName("screen1_2")
        self.horizontalLayout.addWidget(self.screen1_2)
        self.screen1_3 = Channel(self.centralwidget, 3)
        self.screen1_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_3.setText("")
        self.screen1_3.setObjectName("screen1_3")
        self.horizontalLayout.addWidget(self.screen1_3)
        self.screen1_4 = Channel(self.centralwidget, 4)
        self.screen1_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_4.setText("")
        self.screen1_4.setObjectName("screen1_4")
        self.horizontalLayout.addWidget(self.screen1_4)
        self.screen1_5 = Channel(self.centralwidget, 5)
        self.screen1_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_5.setText("")
        self.screen1_5.setObjectName("screen1_5")
        self.horizontalLayout.addWidget(self.screen1_5)
        self.screen1_6 = Channel(self.centralwidget, 6)
        self.screen1_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_6.setText("")
        self.screen1_6.setObjectName("screen1_6")
        self.horizontalLayout.addWidget(self.screen1_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.screen1_7 = Channel(self.centralwidget, 7)
        self.screen1_7.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_7.setText("")
        self.screen1_7.setObjectName("screen1_7")
        self.horizontalLayout_2.addWidget(self.screen1_7)
        self.screen1_8 = Channel(self.centralwidget, 8)
        self.screen1_8.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_8.setText("")
        self.screen1_8.setObjectName("screen1_8")
        self.horizontalLayout_2.addWidget(self.screen1_8)
        self.screen1_9 = Channel(self.centralwidget, 9)
        self.screen1_9.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_9.setText("")
        self.screen1_9.setObjectName("screen1_9")
        self.horizontalLayout_2.addWidget(self.screen1_9)
        self.screen1_10 = Channel(self.centralwidget, 10)
        self.screen1_10.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_10.setText("")
        self.screen1_10.setObjectName("screen1_10")
        self.horizontalLayout_2.addWidget(self.screen1_10)
        self.screen1_11 = Channel(self.centralwidget, 11)
        self.screen1_11.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_11.setText("")
        self.screen1_11.setObjectName("screen1_11")
        self.horizontalLayout_2.addWidget(self.screen1_11)
        self.screen1_12 = Channel(self.centralwidget, 12)
        self.screen1_12.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_12.setText("")
        self.screen1_12.setObjectName("screen1_12")
        self.horizontalLayout_2.addWidget(self.screen1_12)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.screen1_13 = Channel(self.centralwidget, 13)
        self.screen1_13.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_13.setText("")
        self.screen1_13.setObjectName("screen1_13")
        self.horizontalLayout_3.addWidget(self.screen1_13)
        self.screen1_14 = Channel(self.centralwidget, 14)
        self.screen1_14.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_14.setText("")
        self.screen1_14.setObjectName("screen1_14")
        self.horizontalLayout_3.addWidget(self.screen1_14)
        self.screen1_15 = Channel(self.centralwidget, 15)
        self.screen1_15.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_15.setText("")
        self.screen1_15.setObjectName("screen1_15")
        self.horizontalLayout_3.addWidget(self.screen1_15)
        self.screen1_16 = Channel(self.centralwidget, 16)
        self.screen1_16.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_16.setText("")
        self.screen1_16.setObjectName("screen1_16")
        self.horizontalLayout_3.addWidget(self.screen1_16)
        self.screen1_17 = QtWidgets.QLabel(self.centralwidget)
        self.screen1_17.setFrameShape(QtWidgets.QFrame.Panel)
        self.screen1_17.setText("")
        self.screen1_17.setObjectName("screen1_17")
        self.horizontalLayout_3.addWidget(self.screen1_17)
        self.dateEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 18), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.dateEdit, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # self.slrSeekbar = QtWidgets.QSlider(self.centralwidget)
        # self.slrSeekbar.setMaximumSize(QtCore.QSize(16777215, 40))
        # self.slrSeekbar.setOrientation(QtCore.Qt.Horizontal)
        # self.slrSeekbar.setTickPosition(QtWidgets.QSlider.TicksBelow)
        # self.slrSeekbar.setObjectName("slrSeekbar")
        self.slrSeekbar = LabeledSlider(0, 3600 * 24, interval=3600, labels=self.labels, parent=self.centralwidget)
        self.slrSeekbar.sl.setMaximumSize(QtCore.QSize(16777215, 40))
        self.slrSeekbar.sl.setOrientation(QtCore.Qt.Horizontal)
        self.slrSeekbar.sl.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.slrSeekbar.sl.setObjectName("slrSeekbar")
        self.verticalLayout_2.addWidget(self.slrSeekbar)
        self.lblTrajectory = ChannelViewer(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTrajectory.sizePolicy().hasHeightForWidth())
        self.lblTrajectory.setSizePolicy(sizePolicy)
        self.lblTrajectory.setMinimumSize(QtCore.QSize(0, 160))
        self.lblTrajectory.setMaximumSize(QtCore.QSize(16777215, 160))
        self.lblTrajectory.setFrameShape(QtWidgets.QFrame.Box)
        self.lblTrajectory.setText("")
        self.lblTrajectory.setObjectName("lblTrajectory")
        self.verticalLayout_2.addWidget(self.lblTrajectory)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnFastBackward = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFastBackward.sizePolicy().hasHeightForWidth())
        self.btnFastBackward.setSizePolicy(sizePolicy)
        self.btnFastBackward.setMinimumSize(QtCore.QSize(0, 39))
        self.btnFastBackward.setMaximumSize(QtCore.QSize(51, 39))
        self.btnFastBackward.setObjectName("btnFastBackward")
        self.btnFastBackward.clicked.connect(self.onFastBackward)
        self.horizontalLayout_4.addWidget(self.btnFastBackward, 0, QtCore.Qt.AlignTop)
        self.btnPlay = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPlay.sizePolicy().hasHeightForWidth())
        self.btnPlay.setSizePolicy(sizePolicy)
        self.btnPlay.setMinimumSize(QtCore.QSize(0, 39))
        self.btnPlay.setMaximumSize(QtCore.QSize(51, 39))
        self.btnPlay.setObjectName("btnPlay")
        self.btnPlay.clicked.connect(self.onPlay)
        self.horizontalLayout_4.addWidget(self.btnPlay, 0, QtCore.Qt.AlignTop)
        self.btnPause = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPause.sizePolicy().hasHeightForWidth())
        self.btnPause.setSizePolicy(sizePolicy)
        self.btnPause.setMinimumSize(QtCore.QSize(0, 39))
        self.btnPause.setMaximumSize(QtCore.QSize(51, 39))
        self.btnPause.setObjectName("btnPause")
        self.btnPause.clicked.connect(self.onPause)
        self.horizontalLayout_4.addWidget(self.btnPause, 0, QtCore.Qt.AlignTop)
        self.btnFastForward = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFastForward.sizePolicy().hasHeightForWidth())
        self.btnFastForward.setSizePolicy(sizePolicy)
        self.btnFastForward.setMinimumSize(QtCore.QSize(0, 39))
        self.btnFastForward.setMaximumSize(QtCore.QSize(51, 39))
        self.btnFastForward.setObjectName("btnFastForward")
        self.btnFastForward.clicked.connect(self.onFastForward)
        self.horizontalLayout_4.addWidget(self.btnFastForward, 0, QtCore.Qt.AlignTop)
        self.cmbPlayX = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbPlayX.sizePolicy().hasHeightForWidth())
        self.cmbPlayX.setSizePolicy(sizePolicy)
        self.cmbPlayX.setMinimumSize(QtCore.QSize(0, 39))
        self.cmbPlayX.setMaximumSize(QtCore.QSize(16777215, 39))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cmbPlayX.setFont(font)
        self.cmbPlayX.setObjectName("cmbPlayX")
        self.cmbPlayX.addItem("")
        self.cmbPlayX.addItem("")
        self.cmbPlayX.addItem("")
        self.cmbPlayX.addItem("")
        self.cmbPlayX.addItem("")
        self.cmbPlayX.addItem("")
        self.cmbPlayX.addItem("")
        self.cmbPlayX.addItem("")
        self.cmbPlayX.addItem("")
        self.cmbPlayX.addItem("")
        self.horizontalLayout_4.addWidget(self.cmbPlayX, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.setStretch(0, 9)
        self.verticalLayout_3.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1700, 21))
        self.menuBar.setObjectName("menuBar")
        self.menu_File = QtWidgets.QMenu(self.menuBar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menuBar)
        self.mnuFileLoad = QtWidgets.QAction(MainWindow)
        self.mnuFileLoad.setObjectName("mnuFileLoad")
        self.mnuFileLoad.triggered.connect(self.onFileLoad)
        self.menu_File.addAction(self.mnuFileLoad)
        self.menuBar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Additinal Initialization
        self.initChannels()
        self.onPause()
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        self.dateEdit.timeChanged.connect(self.onTimeChanged)
        # self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate.currentDate(), QtCore.QTime(0, 0, 0)))
        self.slrSeekbar.sl.valueChanged.connect(self.slider_value_changed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Surveillance"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "yyyy/M/d HH:mm:ss"))
        self.btnFastBackward.setText(_translate("MainWindow", "<<"))
        self.btnPlay.setText(_translate("MainWindow", ">"))
        self.btnPause.setText(_translate("MainWindow", "| |"))
        self.btnFastForward.setText(_translate("MainWindow", ">>"))
        self.cmbPlayX.setItemText(0, _translate("MainWindow", "2x"))
        self.cmbPlayX.setItemText(1, _translate("MainWindow", "4x"))
        self.cmbPlayX.setItemText(2, _translate("MainWindow", "8x"))
        self.cmbPlayX.setItemText(3, _translate("MainWindow", "16x"))
        self.cmbPlayX.setItemText(4, _translate("MainWindow", "32x"))
        self.cmbPlayX.setItemText(5, _translate("MainWindow", "64x"))
        self.cmbPlayX.setItemText(6, _translate("MainWindow", "128x"))
        self.cmbPlayX.setItemText(7, _translate("MainWindow", "256x"))
        self.cmbPlayX.setItemText(8, _translate("MainWindow", "512x"))
        self.cmbPlayX.setItemText(9, _translate("MainWindow", "1024x"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.mnuFileLoad.setText(_translate("MainWindow", "Load Directory"))

    def onFileLoad(self):
        video_path = str(QtWidgets.QFileDialog.getExistingDirectory(self.MainWindow, "Select Directory"))
        loader = VideoLoader()
        if video_path:
            self.df_origin, ret = loader.load_directory(video_path, self.df_origin, parent=self.MainWindow)
            if ret:
                self.df_origin.to_csv(os.path.join(os.path.dirname(__file__), 'metadata.csv'), index=False)
                print(self.df_origin)

    def onDateChanged(self, dt):
        start_time = datetime.datetime(dt.year(), dt.month(), dt.day(), 0, 0, 0)
        end_time = datetime.datetime(dt.year(), dt.month(), dt.day(), 23, 59, 59)

        self.cur_date = start_time

        duration = (end_time - start_time).seconds
        self.slrSeekbar.sl.setMinimum(0)
        self.slrSeekbar.sl.setMaximum(duration - 1)
        self.slrSeekbar.sl.setTickInterval(duration / 24)
        self.slrSeekbar.sl.setPageStep(3600)
        self.slrSeekbar.sl.setValue(0)

        self.df = self.df_origin
        self.df = self.df[self.df.apply(lambda r: intersect_date(r['start_time'], r['end_time'], start_time, end_time), axis=1)]
        self.df.sort_values(by=['start_time', 'end_time'], inplace=True)
        for channel in self.channels:
            channel.load_metadata(self.df, start_time)

        # if self.df.shape[0] > 0:
        #     self.slrSeekbar.sl.setEnabled(True)
        # else:
        #     self.slrSeekbar.sl.setEnabled(False)

        # self.channel_viewer.draw_tracks(self.df, self.cur_date)
        self.lblTrajectory.set_date_and_data(self.cur_date, self.df)
        self.lblTrajectory.update()
        self.slider_value_changed()
        self.dateEdit.setTime(QtCore.QTime(0, 0, 0))

    def onTimeChanged(self, dt):
        secs = dt.hour() * 3600 + dt.minute() * 60 + dt.second()
        self.slrSeekbar.sl.setValue(secs)
        self.slider_value_changed()

    def slider_value_changed(self):
        secs = self.slrSeekbar.sl.value()
        msecs = secs * 1000
        for channel in self.channels:
            channel.seek_to(msecs)
            channel.update()

        self.dateEdit.blockSignals(True)
        self.dateEdit.setTime(QtCore.QTime(secs // 3600, (secs % 3600) // 60, secs % 60))
        self.dateEdit.blockSignals(False)

    def playVideo(self, direction=0):
        self.btnPlay.setEnabled(False)
        self.btnPause.setEnabled(True)
        self.btnFastBackward.setEnabled(False)
        self.btnFastForward.setEnabled(False)
        self.slrSeekbar.sl.setEnabled(False)
        self.is_playing = True

        start_msecs = self.slrSeekbar.sl.value() * 1000.0
        if direction == 0:
            speedx = 1
        else:
            speedx = pow(2, self.cmbPlayX.currentIndex() + 1) * direction

        elapsed = 0
        while self.is_playing:
            t = time.perf_counter()

            offset_msecs = start_msecs + elapsed
            if (offset_msecs >= self.slrSeekbar.sl.maximum() * 1000 and direction >= 0) or \
                (offset_msecs < self.slrSeekbar.sl.minimum() * 1000 and direction < 0):
                self.onPause()
                break

            for channel in self.channels:
                if direction == 0:
                    channel.step(offset_msecs, 1)
                if direction > 0:
                    channel.step(offset_msecs, speedx)
                if direction < 0:
                    channel.step(offset_msecs, speedx)

            for channel in self.channels:
                channel.update()

            secs = offset_msecs // 1000
            self.slrSeekbar.sl.blockSignals(True)
            self.slrSeekbar.sl.setValue(offset_msecs // 1000)
            self.slrSeekbar.sl.blockSignals(False)

            self.dateEdit.blockSignals(True)
            self.dateEdit.setTime(QtCore.QTime(secs // 3600, (secs % 3600) // 60, secs % 60))
            self.dateEdit.blockSignals(False)

            t1 = (time.perf_counter() - t) * 1000
            delta = 1000 / FPS
            # if speedx > 0:
            #     delta /= speedx
            print('Elapsed: %1.2fms' % t1)
            cv2.waitKey(max(int(delta - t1), 1))
            elapsed += (time.perf_counter() - t) * 1000 * speedx

    def onPlay(self):
        self.playVideo()

    def onFastForward(self):
        self.playVideo(direction=1)

    def onFastBackward(self):
        self.playVideo(direction=-1)

    def onPause(self):
        self.btnPlay.setEnabled(True)
        self.btnPause.setEnabled(False)
        self.btnFastBackward.setEnabled(True)
        self.btnFastForward.setEnabled(True)
        self.slrSeekbar.sl.setEnabled(True)
        self.is_playing = False

    def closeEvent(self, event):
        self.onPause()


class VMainWindow(QtWidgets.QMainWindow):
    ui = None

    def __init__(self, *args, **kwargs):
        super(VMainWindow, self).__init__(*args, **kwargs)

    def closeEvent(self,event):
        if ui is not None:
            ui.onPause()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = VMainWindow()
    ui = Ui_MainWindow(os.path.join(os.path.dirname(__file__), 'metadata.csv'))
    ui.setupUi(MainWindow)
    # ui.initChannels()

    MainWindow.show()
    sys.exit(app.exec_())
