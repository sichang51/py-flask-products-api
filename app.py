import db

from flask import Flask, request

app = Flask(__name__)


@app.route('/products.json')
def index():
    return db.products_all()

@app.route("/products.json", methods=["POST"])
def create():
    image_url = request.form.get("image_url")
    title = request.form.get("title")
    rating = request.form.get("rating")
    description = request.form.get("description")
    cast = request.form.get("cast")
    genre = request.form.get("genre")
    return db.products_create(image_url, title, rating, description, cast, genre)