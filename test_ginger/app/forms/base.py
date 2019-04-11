from flask import request
from wtforms import Form

from app.libs.error_code import ParameterException


class BaseForm(Form):
    def __init__(self):
        args = request.args.to_dict()
        super().__init__(data=request.get_json(silent=True), **args)

    def validate_for_api(self):
        valid = super().validate()
        if not valid:
            raise ParameterException()
        return self
