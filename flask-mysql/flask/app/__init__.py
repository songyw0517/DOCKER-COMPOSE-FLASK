from flask import Flask, jsonify
from app import handler, api
from model import mysql
from flask_cors import CORS
from flask_jwt_extended import *
def create_flask_app(config):
    # application factory 생성
    app = Flask(
        import_name=__name__, # 패키지의 이름
        instance_relative_config=True,
        static_url_path='/', # 정적 폴더 기본 경로 설정
        static_folder='asset/static', # static 폴더 경로 설정
        template_folder='asset/templates'# templates 폴더 경로 설정
        ) 

    # config.py의 환경을 application에 적용한다.
    app.config.from_object(config)

    # cors처리
    CORS(app)

    # api http request handling 설정
    handler.RequestHandler.init_app(app)

    # api error handler 설정
    handler.ErrorHandler.init_app(app)

    # JWT 모듈을 flask 어플리케이션에 등록
    jwt_manager = JWTManager()
    jwt_manager.init_app(app)

    #############################################
    # JWT 콜백 함수 설정 // 이곳에서 하는것인가? #
    #############################################
    # 토큰이 만료되었을 때의 콜백함수
    @jwt_manager.expired_token_loader
    def my_expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            'msg':'token has expired',
            'result': 'fail'
        }), 401


    # # register db connectiong
    mysql.UserModel.register_connection(app)

    app.register_blueprint(api.Index.bp)
    return app
