import cv2
import pytesseract
from PIL import Image
import pdf2image
import math
import xlwt
import glob,os
import shutil
from pdf2image import convert_from_path


pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

allImages = pdf2image.convert_from_path('t1.pdf', output_folder='img/', fmt='jpg')
