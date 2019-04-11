from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, Regexp

from app.forms.base import BaseForm
from app.libs.enums import ClientTypeEnum


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired(message='不允许为空'), length(min=5, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired(message='不允许为空')])

    def validate_type(self, type):
        try:
            client = ClientTypeEnum(type.data)
        except ValueError as e:
            raise e
        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email(message='invalidate email')])
    secret = StringField(validators=[DataRequired(), Regexp(r'^[\w*&$#@]{6,22}$')])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=22)])


class BookSearchForm(BaseForm):
    q = StringField(validators=[DataRequired()])


class TokenForm(BaseForm):
    token = StringField(validators=[DataRequired()])
