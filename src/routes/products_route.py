from flask import request, jsonify, make_response, send_file,send_from_directory
from src.models import Producto
from src.schemas import productSchema, productsSchemas
from app import db
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
import base64
from PIL import Image
import io


#Validaciones De Errores En Busqueda Y Editar
#Crear un Estandar De Respuesta
#Cambiar el manejo de imagenes a base64 para que se puedan subir des de un cliente
#Agregar manejo de formatos PDF

# Estandarizado de Respuesta Listo
def create_product():
    try:
        nombre_product  = request.json['nombre']
        precio_venta    = request.json['precio']
        stock           = request.json['stock']
        image_product   = request.json['image']
        #product_save = productSchema.dump(new_product) 
        
        create_image_base64(image_product, nombre_product)
        
        
        new_product = Producto(nombre_product, precio_venta, stock, nombre_product)
        db.session.add(new_product)
        db.session.commit()

        return jsonify({"success": True, "message": "Product saved successfully"})
    except Exception as ex:
        return jsonify({"success": False, "message": str(ex)})
    


# Estandarizado de Respuesta Listo
def list_products():
    try:
        all_products = Producto.query.all()
        if all_products:
            result = productsSchemas.dump(all_products)
            print(result[1007]['nombre'])
            save_url_image('prueba2')
            
            return jsonify({"success":True, "message":"Products found","data":result})
        else:
            return {"success":False,"message":"Products not found"}
    except Exception as ex:
        return ex

# Estandarizado de Respuesta Listo
def get_product(id):
    try:
        product = Producto.query.get(id)
        if product:
            product_found = productSchema.dump(product)
            return jsonify({"success":True, "message":"Products found","data":[product_found]})
        else:
            return [{"success":False,"message":"Product {0} not found".format(id)}]
    except Exception as ex:
        return ex



# Estandarizado de Respuesta Listo
def update_product(id):
    try:
        product = Producto.query.get(id)
        if product:
            nombre  = request.json['nombre']
            precio  = request.json['precio']
            stock   = request.json['stock']
            image   = request.json['image']

            product.nombre = nombre
            product.precio = precio
            product.stock  = stock
            product.image  = image
            product_update = productSchema.dump(product)

            db.session.commit()
            return jsonify({"success":True,"message":"Product {0} Updated".format(id),"data":[product_update]})
        else:
            return jsonify({"success":False,"message":"Product {0} not found".format(id)})
    except Exception as ex:
        return ex
    

def delete_product(id):
    try:
        product = Producto.query.get(id)
        if(product != None):
            db.session.delete(product)
            db.session.commit()
            return productSchema.jsonify(product)
        else:
            return [{"success":False,"message":"Product {0} not found".format(id)}]
    except Exception as ex:
        return ex
    


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


def create_image_base64(image,name):
    path = '/home/kevin/PersonalProjects/Backend/Python/Flask/flask_api/static/images/{0}.png'.format(name)
    image_bytes = base64.b64decode(image)
    image = Image.open(io.BytesIO(image_bytes))
    image.save(path)
    return image


def save_url_image(image):
    path = '/home/kevin/PersonalProjects/Backend/Python/Flask/flask_api/static/images/'
    print("{0}.png".format(image))
    return send_from_directory(path,image)