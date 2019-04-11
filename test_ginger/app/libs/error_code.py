from .error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    # code = 204
    code = 202
    error_code = 1


class ClientTypeError(APIException):
    code = 400
    msg = (
        "client is invalid"
    )
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class ServerError(APIException):
    code = 500
    msg = 'sorry, we made a mistake (*￣︶￣)!'
    error_code = 999


class NotFound(APIException):
    code = 404
    msg = 'the resource are not found O__O...'
    error_code = 1001


class AuthFailed(APIException):
    code = 401  # 用户名或密码错误的意思
    error_code = 1005
    msg = 'authorization failed'


class Forbidden(APIException):
    code = 403  # 没有权限或被禁止访问
    error_code = 1004
    msg = 'forbidden'


class DuplicateGift(APIException):
    code = 400
    error_code = 2001
    msg = 'the current book has already in gift'
