from flask import request, jsonify, make_response, send_file
from src.models import Producto
from src.schemas import productSchema, productsSchemas
from app import db
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile


#Validaciones De Errores En Busqueda Y Editar
#Crear un Estandar De Respuesta
#Cambiar el manejo de imagenes a base64 para que se puedan subir des de un cliente
#Agregar manejo de formatos PDF

def create_product():
    nombre_product  = request.json['nombre']
    precio_venta    = request.json['precio']
    stock           = request.json['stock']
    image_product   = request.json['image']

    new_product = Producto(nombre_product, precio_venta, stock, image_product)
    db.session.add(new_product)
    db.session.commit()

    return productSchema.jsonify(new_product)

def list_products():
    all_products = Producto.query.all()
 
    result = productsSchemas.dump(all_products)
    print(result)
    return jsonify(result)

def get_product(id):
    product = Producto.query.get(id)
    return productSchema.jsonify(product)

# first function valid is exist data
def update_product(id):
    product = Producto.query.get(id)
    if(product != None):
        nombre  = request.json['nombre']
        precio  = request.json['precio']
        stock   = request.json['stock']
        image   = request.json['image']

        product.nombre = nombre
        product.precio = precio
        product.stock  = stock
        product.image  = image

        db.session.commit()
        return [{"success":True,"message":"Product {0} Updated".format(id)}]
    else:
        return [{"success":False,"message":"Product {0} not found".format(id)}]

def delete_product(id):
    product = Producto.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return productSchema.jsonify(product)


def generate_pdf():
    # Crear un archivo temporal para almacenar el PDF
    temp_pdf = tempfile.NamedTemporaryFile(delete=False)

    # Crear un objeto de lienzo para el PDF
    c = canvas.Canvas(temp_pdf.name, pagesize=letter)

    # Agregar contenido al PDF
    c.drawString(100, 750, "Ejemplo de PDF generado desde Flask")
    c.drawString(100, 730, "Línea 1")
    c.drawString(100, 710, "Línea 2")
    c.drawString(200, 610, "Línea 3")

    # Finalizar el lienzo
    c.save()

    # Devolver el archivo PDF como respuesta
    return send_file(temp_pdf.name, as_attachment=True,download_name="ejemplo.pdf")
