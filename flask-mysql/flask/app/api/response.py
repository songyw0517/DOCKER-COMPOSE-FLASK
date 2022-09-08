"""Response Shortcuts"""
""" Response 정의 """
import json
class Response:
    # 200~ : Success response
    @staticmethod
    def response_ok(result=None):
        return {
            'msg':'success',
            'status_code':200,
            'status_msg':'OK',
            'result': result
        }

    @staticmethod
    def response_no_content(result=None):
        return {
            'msg':'success',
            'status_code':204,
            'status_msg':'No Content',
            'result': result
        }
    
    @staticmethod
    def response_partial_content(result=None):
        return {
            'msg':'success',
            'status_code':206,
            'status_msg':'Partial Content',
            'result': result
        }

    
    # 300~ : Redirection
    @staticmethod
    def response_moved_permanently(result=None):
        pass

    @staticmethod
    def response_found(result=None):
        pass

    @staticmethod
    def response_see_other(result=None):
        pass

    @staticmethod
    def response_not_modified(result=None):
        pass

    @staticmethod
    def response_temporary_redirect(result=None):
        pass

    # 400~ : Client Error
    @staticmethod
    def response_bad_request(result=None):
        return {
            'msg': 'fail',
            'status_code' : 400,
            'status_msg':'Bad Request',
            'result': result
        }
    
    @staticmethod
    def response_unauthorized(result=None):
        return {
            'msg': 'fail',
            'status_code':401,
            'status_msg':'Unauthorized',
            'result': result
        }


    @staticmethod
    def response_forbidden(result=None):
        return {
            'msg': 'fail',
            'status_code':403,
            'status_msg':'Forbidden',
            'result': result
        }

    @staticmethod
    def response_not_found(result=None):
        return {
            'msg': 'fail',
            'status_code':404,
            'status_msg':'Not Found',
            'result': result
        }

    @staticmethod
    def response_method_now_allowed(result=None):
        return {
            'msg': 'fail',
            'status_code':405,
            'status_msg':'Mothod Not Allowed',
            'result': result
        }

    @staticmethod
    def response_conflict(result=None):
        return {
            'msg': 'fail',
            'status_code':409,
            'status_msg':'conflict',
            'result': result
        }

    # 500~ : Server Error
    @staticmethod
    def response_internal_server_error(result=None):
        return {
            'msg': 'fail',
            'status_code':500,
            'status_msg':'Internal Server Error',
            'result': result
        }
    
    @staticmethod
    def response_service_unavailable(result=None):
        return {
            'msg': 'fail',
            'status_code':503,
            'status_msg':'Service Unavailable',
            'result': result
        }
    
    @staticmethod
    def response_gateway_timeout(result=None):
        return {
            'msg': 'fail',
            'status_code':504,
            'status_msg':'Gateway Timeout',
            'result': result
        }
    
    @staticmethod
    def response_http_version_not_supported(result=None):
        return {
            'msg': 'fail',
            'status_code':505,
            'status_msg':'HTTP Version Not Supported',
            'result': result
        }