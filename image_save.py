# -*- coding: UTF-8 -*- #
########################################################
#                                                      #
# Copyright (c) 2023, Mo Dongbao. All Rights Reserved. #
#                                                      #
########################################################

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import multiprocessing
import sys
import os

import cv2
import numpy as np

from kinect_stream import stream, stream_close

jpg_index = 0

if not os.path.exists('jpg'):
    os.makedirs('jpg')

if __name__ == "__main__":
    while True:
        img = stream()
        cv2.imshow("jpg", img)
        key = cv2.waitKey(delay = 1)
        if key == ord('v'):
            cv2.imwrite('jpg/' + str(jpg_index) + '.jpg', img)
            jpg_index = jpg_index + 1
        if key == ord('q'):
            cv2.destroyAllWindows()
            stream_close()
            break

