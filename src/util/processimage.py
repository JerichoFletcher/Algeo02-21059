from PIL import Image
import cv2

def resizeImg(filename):
    img = Image.open(filename)
    return (img.resize((256,256)))

def imgToMatrix(filename):
    return (cv2.imread(filename))
