from sqlalchemy import Column, String, Integer, orm

from app.models.base import Base


class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    # fields = [
    #     'id', 'title', 'author', 'binding', 'publisher',
    #     'price', 'pages', 'pubdate', 'isbn', 'summary', 'image'
    # ]
    # fields 是类属性，所有对象共用类属性

    @orm.reconstructor
    def init_on_load(self):
        self.fields = [
            'id', 'title', 'author', 'binding', 'publisher',
            'price', 'pages', 'pubdate', 'isbn', 'summary', 'image'
        ]
