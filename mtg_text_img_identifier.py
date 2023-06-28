import cv2
import numpy as np
import csv
from difflib import SequenceMatcher
import pytesseract

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def getText(imgnum):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Oliver\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
    gray = cv2.cvtColor(imgnum, cv2.COLOR_BGR2GRAY)
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
    im2 = imgnum.copy()
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cropped = im2[y:y + h, x:x + w]
        text = pytesseract.image_to_string(cropped)
    return text

def imgList():
   names=[]
   with open("mtgcards.csv", 'r') as file:
      csvreader = csv.reader(file)
      for row in csvreader:
         names.append(row)
   return names

def error(img1, img2):
   diff = cv2.subtract(img1, img2)
   err = np.sum(diff**2)
   mse = err/(float(h*w))
   return mse, diff


cam = cv2.VideoCapture(0)
while True:
    check, frame = cam.read()
    cv2.imshow('video', frame)
    key = cv2.waitKey(1)
    if key == ord('c'):
        check, frame = cam.read()
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        break
cam.release()
cv2.destroyAllWindows()

errorList = []
names = imgList()
for i in range(len(names)):
   current = str((names[i][0]))
   img1 = cv2.imread(current+".jpg")
   img1g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
   h, w = img1g.shape
   img2 = cv2.resize(frame, (w, h))
   img2g = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
   match_error12, diff12 = error(img1g, img2g)
   textCard = getText(img2)
   textsim = similar(getText(img1), textCard)
   errorList.append([(match_error12 - (textsim * match_error12)), current, str(names[i][1])])
match = min(errorList)
if match[0] == 0:
    print("The card is", match[2], match[1])
else:
    print("The card is likely", match[2], match[1])
cv2.imshow('image',frame)
cv2.waitKey(0)

