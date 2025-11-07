import math
from flask import Flask, render_template, request, redirect
import dao
from saleapp import app

@app.route("/")

def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page =request.args.get("page")
    prods= dao.load_product(q=q, cate_id=cate_id, page=page)
    pages = math.ceil(dao.count_product()/app.config["PAGE_SIZE"])
    return render_template("index.html", prods=prods, pages=pages)

@app.route("/products/<int:id>")
def details(id):
    prod = dao.get_product_by_id(id)

    return render_template("product-details.html", prod=prod)

@app.route("/login", methods=['get', 'post'])
def login_my_user():

    if request.method.__eq__('post'):
        username = request.form.get("username")
        password = request.form.get("password")

        if username.__eq__("user") and password.__eq__("123"):
            return redirect('/')


    return render_template('login.html')

@app.context_processor
def common_attribute():
    return{
        "cates":dao.load_category()
    }

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)