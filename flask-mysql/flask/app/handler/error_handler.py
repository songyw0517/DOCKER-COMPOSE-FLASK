from werkzeug.exceptions import HTTPException
from app.api.response import Response


class ErrorHandler:
    def init_app(app):
        @app.errorhandler(400)
        def bad_request_error(error: HTTPException):
            """400 Error Handler"""
            return Response.response_bad_request(error.description)


        @app.errorhandler(404)
        def not_found_error(error: HTTPException):
            """404 Error Handler"""
            return Response.response_not_found(error.description)


        @app.errorhandler(500)
        def internal_server_error(error):
            """500 Error Handler (production only)"""
            return Response.response_internal_server_error(error)