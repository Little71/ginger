from flask import current_app
from werkzeug.exceptions import HTTPException

from app import create_app
from app.libs.error import APIException
from app.libs.error_code import ServerError

app = create_app()


@app.errorhandler(Exception)
def framework(e):
    if isinstance(e, APIException):
        return e
    elif isinstance(e, HTTPException):
        return APIException(e.description, e.code, 1007)
    elif current_app.config['DEBUG']:
        raise e
    return ServerError()


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
