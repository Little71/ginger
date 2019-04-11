from flask import current_app, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer, BadSignature, SignatureExpired

from app.forms.forms import ClientForm, TokenForm
from app.libs.auth_token import auth
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import AuthFailed
from app.libs.redprint import Redprint
from app.models.user import User

api = Redprint('token')


@api.route('', methods=['POST'])
def get_token():
    '''return token (带上用户ID, 加密, 时效性)'''
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: User.verify,
    }
    identity = promise[form.type.data](form.account.data, form.secret.data)
    token = generate_auth_token(identity['uid'], form.type.data, identity['scope'],
                                current_app.config['TOKEN_EXPIRATION'])
    return jsonify({'token': token}), 201


@api.route('/secret', methods=['POST'])
def verify_auth_token():
    form = TokenForm().validate_for_api()
    s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(form.token.data,return_header=True)
    except BadSignature:
        raise AuthFailed(msg='token is invalid', error_code=1002)
    except SignatureExpired:
        raise AuthFailed(msg='token is expired', error_code=1003)
    return jsonify({
        'scope': data[0]['scope'],
        'create_at': data[1]['iat'],
        'expire_in': data[1]['exp'],
        'uid': data[0]['uid']
    })


def generate_auth_token(uid, ac_type, scope, expiration=7200):
    s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({'uid': uid, 'type': ac_type.value, 'scope': scope})
