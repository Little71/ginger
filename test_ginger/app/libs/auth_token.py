from collections import namedtuple

from flask import current_app, g
from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired

from app.libs.error_code import AuthFailed

User = namedtuple('User', ['uid', 'ac_type', 'scope'])

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(token, password):
    user_info = verify_auth_token(token)
    g.user = user_info
    return True


def verify_auth_token(token):
    s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    return User(data['uid'], data['type'], data['scope'])
