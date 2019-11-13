import matplotlib.image as mpimg 
import matplotlib.pyplot as plt
import cv2
from PIL import Image, ImageDraw

  
# Read Images 
img = Image.open('final.jpg') 
d = ImageDraw.Draw(img)

left = (0, 70)
right = (2200, 70)
line_color = (0, 0, 255)

num_lines = sum(1 for line in open('../recognizedText.txt'))
print(num_lines)

for i in range(num_lines):
	print(i)
	if i%3 == 0:
		d.line([left, right], fill=line_color, width=2)
		left = (left[0],left[1]+74.5)
		right = (right[0],right[1]+74.5)
img.save("drawn_grid.png")
