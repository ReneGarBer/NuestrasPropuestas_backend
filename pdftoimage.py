#funciona, falta hacerlo de forma general para que lo use un bot
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from pdf2image.generators import counter_generator
import os
import sys
import time
import cv2
import pytesseract
from PIL import Image
from os import listdir
from os.path import isfile, join

def convert(file, outputDir,name):
    #outputDir = outputDir + str(round(time.time())) + '/'
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    #set to convert only the first page of the file
    images = convert_from_path(pdf_path=file,first_page=1,last_page=1,timeout=500)
    counter = 1
    for image in images:
        myfile = outputDir +name+'('+str(counter)+').jpg'
        counter+=1
        image.save(myfile,"JPEG")
        print(myfile)

def mark_region(image_path):
    
    im = cv2.imread(image_path)

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9,9), 0)
    thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)

    # Dilate to combine adjacent text contours
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9,9))
    dilate = cv2.dilate(thresh, kernel, iterations=4)

    # Find contours, highlight text areas, and extract ROIs
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    line_items_coordinates = []
    for c in cnts:
        area = cv2.contourArea(c)
        x,y,w,h = cv2.boundingRect(c)

        if y >= 600 and x <= 1000:
            if area > 10000:
                image = cv2.rectangle(im, (x,y), (2200, y+h), color=(255,0,255), thickness=3)
                line_items_coordinates.append([(x,y), (2200, y+h)])

        if y >= 2400 and x<= 2000:
            image = cv2.rectangle(im, (x,y), (2200, y+h), color=(255,0,255), thickness=3)
            line_items_coordinates.append([(x,y), (2200, y+h)])


    return image, line_items_coordinates

propuestasPDF = r'C:\Users\Usuario\Desktop\Nuestras leyes\propuestas'
files_path = [f for f in listdir(propuestasPDF) if isfile(join(propuestasPDF, f))]
outputDir = r'C:\Users\Usuario\Desktop\Nuestras leyes\imag_before\\'
for file in files_path:
    convert(propuestasPDF+'\\'+file,outputDir,file)

propuestasJPG = r'C:\Users\Usuario\Desktop\Nuestras leyes\imag_before'
image_path = [f for f in listdir(propuestasJPG) if isfile(join(propuestasJPG, f))]
outputDirJPG = r'C:\Users\Usuario\Desktop\Nuestras leyes\imag_after\\'
for path in image_path:
    image,line_items_coordinates = mark_region(propuestasJPG+'\\'+path)
    cv2.imwrite(outputDirJPG+'\\'+path,image)
    print('Imagen guardada en:'+outputDirJPG+'\\'+path)