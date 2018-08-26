import cv2, scipy.misc, time
from PIL import ImageGrab
import numpy as np
from directkeys import *


def grab_screen():
    
    kernel = 5
    grayscreen = np.array(ImageGrab.grab(bbox=(0, 120, 1600, 1300)).convert('L'))
    grayscalesmooth = cv2.GaussianBlur(grayscreen, (kernel, kernel), 0)

    low_thresh = 100
    high_thresh = 200
    edge = cv2.Canny(grayscalesmooth, low_thresh, high_thresh)

    edge_image = scipy.misc.toimage(edge)

    return edge_image


screen_list = []

for i in range(10):
    # grab a screen capture every second for 10
    time.sleep(1)
    screen_list.append(grab_screen())

for im in screen_list:
    im.show()

project64_options = {
    'left' : '0xCB',
    'right' : '0xCD',
    'up' : '0xC8',
    'down' : '0xD0',
    'delete' : '0xD3',
    'pagedown' :  '0xD1',
    'pageup' : '0xC9',
    'home' : '0xC7',
    'end' : '0xCF',
    'num4' : '0x4B',
    'num6' : '0x4D',
    'num8' : '0x48',
    'num2' : '0x50',
    'x' : '0x2D',
    'c' : '0x2E',
    'enter' : '0x1C',
    'a' : '0x1E',
    's' : '0x1F',
    'z' : '0x2C'
}