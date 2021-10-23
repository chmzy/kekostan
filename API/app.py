from flask import Flask, jsonify, request, session
from flask.wrappers import Request
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import pdf_functions
import support_functions


app = Flask(__name__)
CORS(app)

# Роут для склеивания файлов PDF
@app.route('/pdfun/api/v1.0/merge_files', methods=['POST'])
def merge_files():
    data = request.files
    print(data)
    return jsonify({'Answer': 'file on the position'})

# Роут для отправки кода на вебморду
@app.route('/pdfun/api/v1.0/get_code', methods=['GET'])
def get_code():
    return jsonify({'User_code': support_functions.create_code(99,999)})

# Роут для авторизации пользователя по коду
@app.route('/pdfun/api/v1.0/auth_from_code', methods=['POST'])
def auth_from_code():
    return jsonify({'User_code': support_functions.create_code(4)})

@app.route('/pdfun/api/v1.0/send_file_to_web', methods=['POST'])
def send_file_to_web():
    pass

@app.route('/pdfun/api/v1.0/del_file', methods=['POST'])
def del_file():
    pass



if __name__ == '__main__':
    app.run(debug=True)