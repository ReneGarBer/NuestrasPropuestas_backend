from flask import Flask, json, jsonify, request
from db.connection import Database

def run_server():
    app = Flask(__name__)
    bd = Database()

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

    app.run(debug=True)

if __name__ == '__main__':
    run_server()