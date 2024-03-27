from flask import request, jsonify
from src.models import Producto
from src.schemas import productSchema, productsSchemas
from app import db

def create_product():
    nombre_product = request.json['nombre']
    precio_venta = request.json['precio']
    stock = request.json['stock']
    image_product = request.json['image']

    new_product = Producto(nombre_product, precio_venta, stock, image_product)
    db.session.add(new_product)
    db.session.commit()

    return productSchema.jsonify(new_product)

def list_products():
    all_products = Producto.query.all()
    result = productsSchemas.dump(all_products)
    return jsonify(result)

def get_product(id):
    product = Producto.query.get(id)
    return productSchema.jsonify(product)
