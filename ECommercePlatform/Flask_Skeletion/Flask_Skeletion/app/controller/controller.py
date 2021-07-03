from flask import Flask, Blueprint, jsonify, request, json, render_template, url_for, request, redirect, current_app
import flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from ..services.product_list import *
from ..services.product_by_ID import *

uri = Blueprint("endpoint", __name__, url_prefix="/")
uri.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(uri)


# @uri.route("/healthCheck", methods=["GET"])
# def healthCheck():
#     return "Working"

@uri.route("/")
def health_check():
    return "Welcome to E-Commerce Platform"


# Task 1: Retrieve all the business products

@uri.route("/products", methods = ["GET"])
def fetch_product():
    product_list = get_products()
    res = dict()
    if(len(product_list)!=0):
        res['message'] = "All Business Products Retrieved"
        res['product_list'] = product_list
    else:
        res['message'] = "No products to show"
        res['product_list'] = []

    return (jsonify(res),200)

    
# Task 2: Retrieve details of a specific product based on product_id​

@uri.route("/products/<id>", methods = ["GET"])
def fetch_product_by_ID(id):
    product = get_product_by_id(id)
    res = dict()
    if(len(product)!=0):
        res['message'] = "Product Found!"
        res['product_list'] = product
    else:
        res['message'] = "No products to show"
        res['product_list'] = []

    return (jsonify(res),200)
    

# Task 3: Add a product to cart​
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

# Task 4: Delete a product from cart​

# Task 5: List products from cart​

# Task 6: Proceed to Purchase​