class BaseScope:
    allow_api = set()
    allow_redprint = set()
    forbidden_api = set()

    def __add__(self, other):
        self.allow_api |= other.allow_api
        self.allow_redprint |= other.allow_redprint
        self.forbidden_api |= other.forbidden_api
        return self


class SuperScope(BaseScope):
    allow_api = set()

    def __init__(self):
        self + AdminScope() + UserScope()


class AdminScope(BaseScope):
    allow_redprint = {'v1.user'}
    allow_api = {'super_get_user', 'super_del_user'}

    def __init__(self):
        self + UserScope()


class UserScope(BaseScope):
    forbidden_api = {'super_get_user', 'super_del_user'}
    allow_api = set()


def is_in_scope(scope, endpoint: str):
    scope = globals()[scope]
    redprint, fun = endpoint.split('+')
    if fun not in scope.forbidden_api:
        return True
    elif fun in scope.allow_api:
        return True
    elif redprint in scope.allow_redprint:
        return True
    else:
        return False
