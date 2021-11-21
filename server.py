import os
from flask import Flask, json, jsonify, request, send_file
from db.connection import Database
from flask_cors import CORS
from pdftotext import PDFToText

def run_server():
    app = Flask(__name__)
    CORS(app)
    bd = Database()
    pdf_utils = PDFToText()

    @app.route('/api/v0/admin/usuarios', methods=['POST'])
    def usuario():
        if request.method == 'POST' and request.is_json:
            try:
                data = request.get_json()
                print(data)

                if bd.crear_usuario(data['username'], data['password']):
                    return jsonify({'code': 'ok'})
                else:
                    return jsonify({'code': 'existe'})
            except Exception as e:
                print(e)
                return jsonify({'code': 'error'})

 
    @app.route('/api/v0/admin/sesion', methods=['POST'])
    def sesion():
        print(request.is_json, request.method)
        if request.method == 'POST' and request.is_json:
            try:
                data = request.get_json()
                username = data['username']
                password = data['password']

                id, ok = bd.iniciar_sesion(username, password)

                if ok:
                    return jsonify({'code': 'ok', 'id': id})
                else:
                    return jsonify({'code': 'noexiste'})
            except Exception as e:
                print(e)
                return jsonify({'code': 'error'})

    @app.route('/api/v0/file/<string:filename>', methods=['GET'])
    def get_file(filename = None):
        if request.method == 'GET' and filename is not None:
            return send_file(pdf_utils.file_path(filename), as_attachment=False)


    @app.route('/api/v0/admin/files', methods=['POST'])
    def read_file():
        if request.method == 'POST':
                
            if 'files[]' not in request.files:
                return jsonify({'code': 'nofile'})
                
            files = request.files.getlist('files[]')

            done, filename, extract = pdf_utils.read_file(files)
            if done:
                return jsonify({
                    'code': 'ok', 
                    'pdf': filename, 
                    'ocr': filename + '.txt',
                    'extract': extract 
                    })
            else:
                return jsonify({'code': 'fail'})

    @app.route('/api/v0/admin/propuesta/<int:id>', methods=['PATCH'])
    @app.route('/api/v0/admin/propuesta', methods=['POST'])
    def propuestas(id = None):
        if request.method == 'POST' and id is None:
            data = request.get_json()
            print(data)
            
            if bd.nueva_propuesta(data):
                return jsonify({'code': 'ok'})
            else:
                return jsonify({'code': 'fail'})

    app.run(debug=True)

if __name__ == '__main__':
    run_server()