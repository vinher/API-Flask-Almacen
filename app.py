from flask import Flask
from src.models import db
from src.schemas import ma
from src.routes.products_route import *
from src.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)


    #Manejo Tabla Usuarios Implementar
    app.route('/add/user'           , methods=['POST'])  (create_product)
    app.route('/update/user'        , methods=['PUT'])   (list_products)
    app.route('/delete/user/<id>'   , methods=['DELETE'])(get_product)
    app.route('/all/user/<id>'      , methods=['GET'])   (update_product)
    app.route('/search/user/<id>'   , methods=['GET'])   (delete_product)
    app.route('/generate/users'     , methods=['GET'])   (generate_pdf)


    #Manejo de tabla productos
    app.route('/add/product'        , methods=['POST'])  (create_product)
    app.route('/list/product'       , methods=['GET'])   (list_products)
    app.route('/list/product/<path:filename>'       , methods=['GET'])   (save_url_image)
    app.route('/search/product/<id>', methods=['GET'])   (get_product)
    app.route('/update/product/<id>', methods=['PUT'])   (update_product)
    app.route('/delete/product/<id>', methods=['DELETE'])(delete_product)
    app.route('/generate/pdf'       , methods=['GET'])   (generate_pdf)

    #Manejo Tabla Clientes




    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0',debug=True)
