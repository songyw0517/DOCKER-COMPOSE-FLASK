from flask import Blueprint, render_template, request, current_app
from model import mysql
from app.api.response import Response

class Index:
    bp = Blueprint('index', __name__)

    @bp.route('/')
    def index():
        return render_template('index.html')

    @bp.route('/response_test')
    def res_test():
        return Response.response_200()
    
    @bp.post('/insert_user')
    def insert():
        data = request.get_json()
        current_app.logger.info(data)
        model = mysql.UserModel()
        result = model.user_sign_up(["test","test","test","test","test","test"])
        return result