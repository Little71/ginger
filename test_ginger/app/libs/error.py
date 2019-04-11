import json

from flask import request
from werkzeug.exceptions import HTTPException

class APIException(HTTPException):
    code = 500
    msg = 'sorry, we made a mistake'
    error_code = 999

    def __init__(self,msg=None,code=None,error_code=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code

        super(APIException, self).__init__(msg, None)


    def get_body(self, environ=None):
        '''return {“msg”:"xxx", "error_code":1000,"request":url}'''
        return json.dumps(dict(
            msg = self.msg,
            error_code=self.error_code,
            request = '{} {}'.format(request.method,request.full_path.strip('?')[0])
        ))

    def get_headers(self, environ=None):
        """Get a list of headers."""
        return [('Content-Type', 'application/json')]