import os
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os  
from shutil import copyfile
from random import randint

class PDFToText:
    def __init__(self):
        self.ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def file_path(self, filename, folder = 'upload'):
        return os.path.join( os.getcwd() + '/' + folder + '/' + filename)

    def read_file(self, files):
        file = files[0]

        saved, path = self.save_file(file)

        print('Path: ' + path)

        if saved is False:
            return False

        pages = self.to_image(path)
        print('Pages: ' + str(pages))

        if pages <= 0:
            return False 

        done, extract = self.ocr(pages)
        
        return done, self.filename, extract

    def save_file(self, file):
        if file and self.allowed_file(file.filename):
            secure = secure_filename(file.filename)
            filename = str(randint(0,9999)) + '_' + secure
            self.filename = filename
            path = os.path.join( os.getcwd() + '/upload/' + filename)
            copy = os.path.join( os.getcwd() + '/upload/' + secure)
            file.save(os.path.join( os.getcwd() + '/upload/' + filename))
            copyfile(path, copy)
            return True, path
        else:
            return False, None

    def to_image(self, path):
        pages = convert_from_path(path, 500)
        image_counter = 0

        for page in pages:
    
            filename = "temp/page_"+str(image_counter)+".jpg"      
            page.save(filename, 'JPEG')
            image_counter = image_counter + 1

        return image_counter

    def ocr(self, count):
        try:
            file_limit = count
            outfile = 'upload/' + self.filename + '.txt'

            with open(outfile, 'w', encoding='utf-8') as f:
                for i in range(file_limit):
                    filename = "temp/page_"+str(i)+".jpg"
                    text = str(((pytesseract.image_to_string(Image.open(filename)))))

                    print(text)

                    if i == 0:
                        extract = text

                    text = text.replace('-\n', '')    
                    f.write(text)

            return True, extract
        except Exception as e:
            print(e)
            return False, None

    def read_content(self, filename):
        with open(self.file_path(filename),'r', encoding='utf-8') as f:
            text = f.read()
        return text

    def copy_to_upload(self, origin, folder):
        origin_path = self.file_path(origin, folder)
        dest_path = self.file_path(origin)
        copyfile(origin_path, dest_path)
