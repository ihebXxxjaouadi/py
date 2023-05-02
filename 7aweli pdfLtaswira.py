 
import PyPDF2
from PyPDF2 import PdfReader
import csv
import re
import requests
import pandas as pd
from collections import namedtuple
import os
import fitz
from PIL import Image
import cv2
import easyocr


try :
    if(os.path.exists(os.path.join('./', 'data.txt'))) :
        print("file data.txt is exist you should delete it to complete the operation")
    else :

        print('hi1')
        print('hi1')

        pdf_file = open('cv.pdf', 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        print( num_pages)

        reader = PdfReader("cv.pdf")
        print(pdf_reader.pages[0])
        print('hi1')

        for page in pdf_reader.pages[1:30]:

            dat=page.extract_text()
            print('hi0')

            if (dat) :
                print('hi1')
                with open("data.txt","w") as file:
                    print('hi2')

                    file.write(dat)


except:
    print('hi3')

    directory = "images"

    parent_dir = "./"

    path = os.path.join(parent_dir, directory)
    if (os.path.exists(path)) :
        print("floder 'images' exits you should delete it to complete the operation")
    else :
        os.mkdir(path)
        print("Directory '% s' created" % directory)
        print('scaning ...')

        file_path = 'cv.pdf'

        images_path = './images/'




        pdf_file = fitz.open(file_path)

        page_nums = len(pdf_file)

        images_list = []

        for page_num in range(page_nums):
            page_content = pdf_file[page_num]
            images_list.extend(page_content.get_images())

        if len(images_list)==0:
            raise ValueError(f'No images found in {file_path}')

        for i, img in enumerate(images_list, start=1):
            xref = img[0]
            base_image = pdf_file.extract_image(xref)
            image_bytes = base_image['image']
            image_ext = base_image['ext']
            image_name = str(i) + '.' + image_ext
            with open(os.path.join(images_path, image_name) , 'wb') as image_file:
                image_file.write(image_bytes)
                image_file.close()



        img = cv2.imread('./images/1.png')

        reader = easyocr.Reader(['fr'], gpu=False)

        result = reader. readtext(img)
        detctedText= ''
        for text in result:

            detctedText = detctedText + '\n' +text [1]
            if(detctedText):
                with open("data.txt","w") as file:
                    file.write(detctedText)

