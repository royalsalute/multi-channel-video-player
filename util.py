import cv2

import datetime
import threading
import numpy as np
import pandas as pd

from PyQt5 import QtCore, QtGui, QtWidgets

NUM_CHANNEL = 16
FPS = 12.0


def get_qimage(image):
    height, width, colors = image.shape
    bytesPerLine = 3 * width
    QImage = QtGui.QImage

    image = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)

    image = image.rgbSwapped()
    return image


def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized