import json
from itertools import product
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from saleapp import db, app
from flask_login import UserMixin
import enum
from enum import Enum as RoleEnum

class UserRole(enum.Enum):
    USER = 1
    ADMIN = 2

class Base(db.Model):
    __abstract__=True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500), nullable=False)
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    def __str__(self):
        return self.name

class User(Base, UserMixin):
    username = Column(String(150), unique=True, nullable=False)
    password = Column(String(150), nullable=False)
    avatar = Column(String(300), default="http://weart.vn/wp-content/uploads/2025/06/anh-den-phan-anh-chieu-sau-noi-tam.jpg")
    role = Column(Enum(UserRole), nullable=False, default=UserRole.USER)

class Category(Base):
    products = relationship('Product', backref="category", lazy=True)


class Product(Base):
    image = Column(String(500),default="https://24hstore.vn/images/products/2025/09/11/large/iphone-17-pro-max-cam-nb_1757564962.jpg")
    price = Column(Float, default=0.0)
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    description = Column(Text)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

        # c1 = Category(name="Laptop")
        # print(c1)
        # c2 = Category(name="Mobile")
        # c3 = Category(name="Tablet")
        #
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()
        #
        # with open("data/product.json", encoding="utf-8") as f:
        #     products = json.load(f)
        #
        #     for p in products:
        #         db.session.add(Product(**p))


        import hashlib

        u = User(name="User", username="user", password=str(hashlib.md5("123".encode("utf-8")).hexdigest()))

        db.session.add(u)

        db.session.commit()
