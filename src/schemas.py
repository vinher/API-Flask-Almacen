from flask_marshmallow import Marshmallow

ma = Marshmallow()

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('nombre', 'precio', 'stock', 'imagen')

productSchema = ProductSchema()
productsSchemas = ProductSchema(many=True)
