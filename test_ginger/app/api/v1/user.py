from flask import g
from flask.json import jsonify

from app.libs.auth_token import auth
from app.libs.error_code import DeleteSuccess
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.user import User

api = Redprint('user')


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    return jsonify(User.query.get_or_404(uid))


@api.route('', methods=['DELETE'])
@auth.login_required
def del_user():
    with db.auto_commit():
        uid = g.user.uid
        User.query.get_or_404(uid).delete()
    return DeleteSuccess()


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_del_user(uid):
    with db.auto_commit():
        User.query.get_or_404(uid).delete()
    return DeleteSuccess()
