'''
Application Config Setting
'''
import os
from datetime import timedelta
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class Configbase:
    APP_NAME = "FLASK_MYSQL"

# TestConfig 클래스
class TestConfig(Configbase):
    DEBUG = True
    TESTING = True
    DATABASE_CONFIG = {
        # host는 mysql 컨테이너 이름으로 설정합니다.
        "host": "mysql",
        "port": "3306",
        "database": "SEGORANG",
        "user": "root",
        "password":"scof",
        "pool_name":"mypool",
        "pool_size":3,
    }

    # JWT 설정
    JWT_TOKEN_LOCATION = ["headers", "cookies"]
    JWT_COOKIE_SECURE = False
    JWT_SECRET_KEY = 'ginkscof'
    
    @staticmethod
    def init_app(app):
        pass



config=TestConfig