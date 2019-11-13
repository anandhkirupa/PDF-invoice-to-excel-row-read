import pytesseract
from PIL import Image
import cv2
import sys
import math


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
file = open("recognizedText.txt", "w")

img = cv2.imread("a4.jpg")
cropped = img[181:1700, 0:2200]
cv2.imwrite("cropped.jpg",cropped)
gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
thresh, blackAndWhiteImage = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
edges = cv2.Canny(blackAndWhiteImage, 80, 120, thresh)
lines = cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1)
print(lines)
if lines != "None":
	for line in lines[0]:
		pt1 = (line[0],line[1])
		pt2 = (line[2],line[3])
	#	cv2.line(img, pt1, pt2, (0,0,255), 1)
		print(pt1, pt2)
	#	cv2.imwrite("temp2.jpg", img)
	flag = 1
	print("found if")
	#cropped1 = cropped[175:1700, 0:]
	cropped1 = cropped[0:pt1[1],0:2200]
	cv2.imwrite("final.jpg",cropped1)
	colC = cropped1[0:1000,320:450]
	cv2.imwrite("colC.jpg",colC)

	text = str(((pytesseract.image_to_string(Image.open("colC.jpg")))))

	print(type(text))
	file.write(text)
	file.close()


	num_lines = sum(1 for line in open('recognizedText.txt'))
	print(num_lines)
else:
	colC = cropped[0:1000,320:450]
	cv2.imwrite("colC.jpg",colC)

	text = str(((pytesseract.image_to_string(Image.open("colC.jpg")))))

	print(type(text))
	file.write(text)
	file.close()


	num_lines = sum(1 for line in open('recognizedText.txt'))
	print(num_lines)