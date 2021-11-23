from logging import error
from bot_download import bot_scraping as bot
import requests, pdf2image, pytesseract, cv2
from db.connection import Database
from pdftotext import PDFToText
#direccion de driver
path = r'C:\chromedriver_win32\chromedriver.exe'

error_text = "El citado documento no se publica"

robot = bot(path)
db = Database()
pdfutils = PDFToText()

robot.open_page('https://congresoweb.congresojal.gob.mx/infolej/sistemaintegral/infolej/iniciopw.cfm','Documento sin título')

robot.select_option('','name','C_Legis')

tipos = {
    '23':'Acuerdo interno',
    '17':'Acuerdo Legislativo',
    '1':'Acuerdos Administrativos',
    '9':'Comunicaciones de Particulares',
    '8':'Comunicaciones de Tramite Legislativo',
    '7':'Denuncia de Juicio Político',
    '19':'Dictamen de Acuerdo',
    '14':'Dictamen de Decreto',
    '4':'Iniciativa de Acuerdo Legislativo',
    '5':'Iniciativa de Decreto',
    '6':'Iniciativa de Ley',
    '3':'Minuta de Acuerdo Legislativo',
    '2':'Minuta de Decreto',
    '12':'Suspension de Cargo',
    '21':'Votos Constitucionales'
    }

#direccion de carpeta
folder = r'pdf_txt_files'

#busca links por cada tipo
try:
    for value in tipos:
        robot.select_option(value,'id','C_Tipo')
        robot.click_button('name','Submit')
        links = robot.find_pdf_links()

        #itera sobre los links obtenidos
        for i, link in enumerate(links):

            if i == 50: #Para que no suba todo
                break

            pdf = requests.get(link,stream=True)
            name = link.rsplit('/',1)[-1]
            with open(folder+'\\'+name, 'wb') as f:
                f.write(pdf.content)
            
            image = pdf2image.convert_from_bytes(pdf.content,first_page=1,last_page=1)
            #tal vez exista una manera de acerlo sin guardar la imagen
            image[0].save(folder+'\\'+name+'.jpg','JPEG')
            image = cv2.imread(folder+'\\'+name+'.jpg')
            custom_config = r'--oem 3 --psm 1'
            # problemas con characteres desconocidos que no puede guardar
            text = pytesseract.image_to_string(image, config=custom_config)


            with open(folder+'\\'+name+'.txt', 'w', encoding='utf-8') as f:
                texto = tipos[value] + '. \n\n'+ text
                f.write(texto)
            
            if error_text not in text:
                pdfutils.copy_to_upload(name, folder )
                pdfutils.copy_to_upload(name + '.txt', folder)

                data = {
                    'titulo': 'Sobre ' + tipos[value] + ': ' + name,
                    'extracto': text,
                    'pdf': name,
                    'estado': 'Desconocido',
                    'partido': 'Pendiente',
                    'fecha': '2021-11-01',
                    'autor': 'Subido desde bot',
                    'subido': '4'
                }

                print(data)
                db.nueva_propuesta(data)
                print('New record added!')
            else:
                print('Record skipped')
except:
    pass

robot.close_window()