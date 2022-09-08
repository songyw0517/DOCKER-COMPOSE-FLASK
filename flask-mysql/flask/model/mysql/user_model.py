from .mysql_model import MysqlModel
from .user_model_interface import UserModelInterface
from flask import current_app
import model
class UserModel(MysqlModel, UserModelInterface):
    def __init__(self) -> None:
        super().__init__()

    # 회원 가입
    def user_sign_up(self, user_data:list):
        db = self.get_connection()
        conn = db.get_connection()
        cursor = conn.cursor()
        add_user_query = ("INSERT INTO user"
                        "(user_sj_id, user_id, user_pw, user_name, user_major, user_nickname)"
                        "VALUES (%s, %s, %s, %s, %s, %s)")
        try:
            msg = cursor.execute(add_user_query, user_data)
            current_app.logger.warning("회원가입이 완료되었습니다.")
            conn.commit()
            return model.ModelResponse.response_ok(msg)

        except Exception as e:
            return model.ModelResponse.response_err(e)

    '''
    {key : value}를 입력받아,
    user 테이블로부터 key column = value인 값을 찾는다.
    '''
    def find_one_col_by_value(self, col, value:dict):
        db = self.get_connection()
        conn = db.get_connection()
        cursor = conn.cursor()
        col_name, col_value = list(value.items()).pop()
        current_app.logger.info("{} : {}".format(col_name, col_value))
        query = '''
                SELECT {}
                FROM user
                WHERE {}="{}"
                '''.format(col, col_name, col_value)
        try:
            current_app.logger.info(query)
            cursor.execute(query)
            result = cursor.fetchone()
            current_app.logger.info(result)
            return model.ModelResponse.response_ok(result)
        except Exception as e:
            return model.ModelResponse.response_err(e)

    
    def delete_user_by_dict(self, rm_data:dict):
        db = self.get_connection()
        conn = db.get_connection()
        cursor = conn.cursor()

        col_name, col_value = list(rm_data.items()).pop()
        query = '''
                DELETE
                FROM user
                WHERE {}="{}"
                '''.format(col_name, col_value)
        try:
            cursor.execute(query)
            conn.commit()
            return model.ModelResponse.response_ok()
        except Exception as e:
            return model.ModelResponse.response_err(e)