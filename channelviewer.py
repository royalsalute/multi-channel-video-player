import numpy as np
import cv2
import datetime
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

from util import image_resize, get_qimage

NUM_CHANNEL = 16

color_start = np.array([0, 0, 255])
color_end = np.array([0, 255, 255])

class ChannelViewer(QtWidgets.QLabel):
    cur_date = None
    df = pd.DataFrame()

    def __init__(self, parent, *args, **kwargs):
        super(ChannelViewer, self).__init__(parent)

    def set_date_and_data(self, cur_date, df):
        self.cur_date = cur_date
        self.df = df

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        w = self.frameGeometry().width()
        h = self.frameGeometry().height()

        img = np.zeros([h, w, 3], dtype=np.uint8)
        img[:, :] = (240, 240, 240)

        th = h / NUM_CHANNEL
        thstep = th / 2

        w_t = 3600 * 24
        for i in self.df.index:
            row = self.df.loc[i]

            from_sec = (max(row['start_time'], self.cur_date) - self.cur_date).seconds
            to_sec = (row['end_time'] - self.cur_date).total_seconds()
            x1 = int(from_sec * w / w_t)
            x2 = int(to_sec * w / w_t)
            y = int((row['channel'] - 1) * h / NUM_CHANNEL + thstep)

            color = (color_end - color_start) * (row['channel'] - 1) // NUM_CHANNEL + color_start
            img = cv2.line(img, (x1, y), (x2, y), (int(color[0]), int(color[1]), int(color[2])), 2)

        img = cv2.rectangle(img, (0, 0), (img.shape[1] - 1, img.shape[0] - 1), (64, 64, 64), 1)

        painter.drawImage(QtCore.QPoint(0, 0), get_qimage(img))
