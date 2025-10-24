import json
from itertools import product

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from saleapp import db, app

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500), nullable=False, unique=True)
    products = relationship('Product', backref="category", lazy=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(500), nullable=False, unique=True)
    image = Column(String(500), default="https://24hstore.vn/images/products/2025/09/11/large/iphone-17-pro-max-cam-nb_1757564962.jpg")
    price = Column(Float, default=0.0)
    cate_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__=="__main__":
    with app.app_context():
        # db.create_all()
        #
        # c1 = Category(name="Laptop")
        # c2 = Category(name="Mobile")
        # c3 = Category(name="Tablet")

        db.session.add_all([c1,c2,c3])
        db.session.commit()

        with open("data/product.json", encoding="utf-8") as f:
            products = json.load(f)

            for p in products:
                db.session.add(Product(**p))

            db.session.commit()