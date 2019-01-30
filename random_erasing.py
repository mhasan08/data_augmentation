import numpy as np
import cv2

import random
import math


'''
https://arxiv.org/pdf/1708.04896.pdf
'''

def erase(img):
    height, width, channels = img.shape

    #p = 0.6
    ratios = [0.3, 0.2]
    S = height * width
    s_l = 0.02
    s_h = 0.04
    r2 = ratios[random.randint(0, 100) % 2]
    r1 = ratios[random.randint(0, 100) % 2]
    scaled_dim = []
    scaled_dim.append(s_l)
    scaled_dim.append(s_h)

    scaled_ratio = []
    scaled_ratio.append(r1)
    scaled_ratio.append(r2)
    
    while True:
        S_e = int(scaled_dim[(random.randint(0,9) % 2)] * S)
        r_e = scaled_ratio[(random.randint(0,100) % 2)]

        H_e = int(math.sqrt(S_e * r_e))
        W_e = int(math.sqrt(S_e / r_e))

        x_e = random.randint(0, width)
        y_e = random.randint(0, height)

        if x_e + W_e <= width and y_e + H_e <= height and int(S / S_e) >= 50:
            color = random.randint(0, 256)
            cv2.rectangle(img, (x_e, y_e), (W_e, H_e), (color, color, color), -1)
            return img

