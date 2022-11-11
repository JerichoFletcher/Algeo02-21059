from PIL import Image
import numpy as np
import cv2

def resizeImg(filename):
    img = Image.open(filename)
    return (img.resize((256,256)))

def imgToMatrix(filename):
    return (cv2.imread(filename))

def RGBtoGrayscale(imagemat):
    return (cv2.cvtColor(imagemat, cv2.COLOR_BGR2GRAY))

def loadImg(filename):
    img = resizeImg(filename)
    imgmat = np.asarray(img)
    return RGBtoGrayscale(imgmat)
