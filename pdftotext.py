import os 
from werkzeug.utils import secure_filename

class PDFToText:
    def __init__(self):
        self.ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def read_file(self, files):
        file = files[0]
        if file and self.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join( os.getcwd() + '/upload/' + filename))
            return True
        else:
            return False
