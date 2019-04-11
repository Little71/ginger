from app.forms.forms import ClientForm, UserEmailForm
from app.libs.enums import ClientTypeEnum
from app.libs.error_code import Success
from app.libs.redprint import Redprint
from app.models.user import User

api = Redprint('client')

@api.route('/register',methods=['POST'])
def register():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL:__register_by_email,
        ClientTypeEnum.USER_MOBILE:__register_by_mobile,
    }
    promise[form.type.data]()
    return Success()


def __register_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,form.account.data,form.secret.data)

def __register_by_mobile():
    pass