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
    #Manejo de tabla producto
    app.route('/add/product'        , methods=['POST'])  (create_product)
    app.route('/list/product'       , methods=['GET'])   (list_products)
    app.route('/search/product/<id>', methods=['GET'])   (get_product)
    app.route('/update/product/<id>', methods=['PUT'])   (update_product)
    app.route('/delete/product/<id>', methods=['DELETE'])(delete_product)
    app.route('/generate/pdf'       , methods=['GET'])   (generate_pdf)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
