from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery

# SQLAlchemy对象
from sqlalchemy import Column, SmallInteger, Integer

from app.libs.error_code import NotFound


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            db.session.commit()
        except Exception as e:
            db.session.rollback()  # 回滚，都失效，相当于都没执行
            raise e


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)

    def get_or_404(self, ident):
        rv = self.get(ident)
        if rv is None:
            raise NotFound()
        return rv

    def first_or_404(self):

        rv = self.first()
        if rv is None:
            raise NotFound()
        return rv


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True  # 抽象模型，不会生成真正的表
    create_time = Column(Integer)
    status = Column(SmallInteger, default=1)  # 是否有效数据 0 不生效  1 生效

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def __getitem__(self, item):
        return getattr(self, item)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def keys(self):
        return self.fields

    def hide(self, *keys):
        self.fields -= set(keys)
        return self

    def append(self, *keys):
        self.fields |= set(keys)
        return self
