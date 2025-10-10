from flask import Flask, render_template, request
import dao

app = Flask(__name__)


@app.route("/")

def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    cates = dao.load_category()
    prods= dao.load_product(q=q, cate_id=cate_id)
    return render_template("index.html", cates=cates, prods=prods)

if __name__ == "__main__":
    app.run(debug=True)