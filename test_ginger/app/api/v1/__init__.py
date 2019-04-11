from flask import Blueprint

from app.api.v1 import book, client, token, user,gift


def create_blueprint():
    bp = Blueprint('v1',__name__)
    book.api.register(bp)
    client.api.register(bp)
    token.api.register(bp)
    user.api.register(bp)
    gift.api.register(bp)
    return bp