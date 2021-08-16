# ocr recognition

import pytesseract
from PIL import Image
import cv2 as cv
import numpy as np

img = cv.imread('./test.png')

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_img = cv.medianBlur(gray_img, 3)
# img = cv.Canny(img, 200, 200)

cv.imshow('img', gray_img)
cv.waitKey(0)

# text = pytesseract.image_to_string(img)
# print(text)
