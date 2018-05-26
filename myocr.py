from PIL import Image
import pytesseract
import argparse
import cv2
import os
pim=cv2.imread('sam5.jpeg')
gim=cv2.cvtColor(pim,cv2.COLOR_BGR2GRAY)
gim=cv2.threshold(gim,0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)[1]
filename="{}.png".format(os.getpid())
cv2.imwrite(filename,gim)
text=pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
cv2.waitKey(0)
