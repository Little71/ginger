from flask import jsonify

from app.forms.forms import BookSearchForm
from app.libs.redprint import Redprint
from app.models.book import Book

api = Redprint('book')


@api.route('/search')
def search():
    form = BookSearchForm().validate_for_api()
    q = f'%{form.q.data}%'
    books = Book.query.filter_by((Book.title.like(q)) | (Book.publisher.like(q))).all()
    return jsonify([book.hide('summary') for book in books])


@api.route('/<isbn>/detail')
def detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)
