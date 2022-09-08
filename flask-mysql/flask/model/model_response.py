"""
모델에서의 응답을 정의합니다.

{
    'result' : 'success' 또는 'fail'입니다.
    'error':{
        'error_type' : 발생한 에러의 타입
        'error_no' : 발생한 에러의 번호
        'sql_state' : sql에서 발생한 에러의 번호
        'error_msg' : 전반적인 에러 메시지
        'error_details' : 자세한 에러 메시지
    },
    'msg' : 추가 메시지
}
"""
class ModelResponse:
    @staticmethod
    def response_ok(model_msg=None):
        return {
            'result':'success',
            'details':'ok',
            'model_msg':model_msg
        }
    
    @staticmethod
    def response_err(error:Exception, msg=None):
        return {
            'result':'fail',
            'error':{
                'error_type' : type(error).__name__,
                'error_no' : error.__dict__.get('errno', None),
                'sql_state' : error.__dict__.get('sqlstate', None),
                'error_msg' : error.__doc__
            },
            'msg' : msg
        }