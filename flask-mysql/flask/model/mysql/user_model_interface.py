from abc import ABCMeta, abstractmethod
from .mysql_model import MysqlModel

"""
user model의 기능 명시
"""
class UserModelInterface(metaclass=ABCMeta):
    """
    function description
    --------------------
    사용자 정보를 입력받아 user 테이블에 사용자를 등록합니다.

    Params
    --------
    dict = {
        "user_id":"DevScof",
        "user_pw":"testtest",
        "user_name":"김블라",
        "user_email":"songyw0517@naver.com",
        "user_nickname":"scof",
        "user_create_at":"2022-05-17 19:27:12"
    }

    Return
    --------
    Bool (True or False)
    """
    @abstractmethod
    def user_sign_up(user_data:dict):
        pass
