import cv2
import numpy as np
import os

import random
import string
import time

from random_erasing import erase

def renameImages():
    raw_image_dir = "./cat/"
    base_image_dir = "./base_images/"

    for rawImageName in os.listdir(raw_image_dir):
        img = cv2.imread(raw_image_dir + rawImageName)
        name = random.randint(10000, 10000000000000)
        cv2.imwrite(base_image_dir + str(name) +".png", img)
        time.sleep(0.01)


def applyLuminosity(img):
    lusimage = np.zeros(img.shape, img.dtype)
    alpha = 2.2
    beta = 25.0
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            for c in range(img.shape[2]):
                lusimage[y,x,c] = np.clip(alpha*img[y,x,c] + beta, 0, 255)
    return lusimage


def mirrorImage(img):
    return cv2.flip(img, 1)

def bgrImage(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


def gaussianBlur(img):
    kernel = np.ones((5,5),np.float32)/25
    return cv2.filter2D(img,-1,kernel)


def bilateralFilter(img):
    kernel = np.ones((5,5),np.float32)/25
    return cv2.bilateralFilter(img,9,75,75)


def applyClahe(img):
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))
    return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)


def augumentData(mirror, luminosity, bgr, blur, clahe, random_erase):
    print("start")
    base_image_dir = "./base_images/"
    augmented_image_dir = "./augmented_images/"

    for baseImage in os.listdir(base_image_dir):
        print(baseImage)
        img = cv2.imread(base_image_dir + baseImage)
        if mirror == True:
            flippedImage = mirrorImage(img)
            rs = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
            newImageName = str(random.randint(10, 1000000)) + rs + ".png"
            cv2.imwrite(augmented_image_dir + newImageName, flippedImage)
        if luminosity == True:
           lusimage = applyLuminosity(img)
           rs = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
           newImageName = str(random.randint(10, 1000000)) + rs + ".png"
           cv2.imwrite(augmented_image_dir + newImageName, lusimage)
        if bgr == True:
            bgrImageData = bgrImage(img)
            rs = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
            newImageName = str(random.randint(10, 1000000)) + rs + ".png"
            cv2.imwrite(augmented_image_dir + newImageName, bgrImageData)
        if blur == True:
            gaussianImage = gaussianBlur(img)
            rs = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
            newImageName = str(random.randint(10, 1000000)) + rs + ".png"
            cv2.imwrite(augmented_image_dir + newImageName, gaussianImage)

            bilateralImage = bilateralFilter(img)
            rs = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
            newImageName = str(random.randint(10, 1000000)) + rs + ".png"
            cv2.imwrite(augmented_image_dir + newImageName, bilateralImage)
        if clahe == True:
            claheImage = applyClahe(img)
            rs = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
            newImageName = str(random.randint(10, 1000000)) + rs + ".png"
            cv2.imwrite(augmented_image_dir + newImageName, claheImage)
        if random_erase == True:
            erasedImage = erase(img)
            rs = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
            newImageName = str(random.randint(10, 1000000)) + rs + ".png"
            cv2.imwrite(augmented_image_dir + newImageName, erasedImage)


augumentData(mirror=True, luminosity=True, bgr=True, blur=True, clahe=True, random_erase=True)

