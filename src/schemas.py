from flask_marshmallow import Marshmallow

ma = Marshmallow()

class ProductSchema(ma.Schema):
    class Meta:
        #Campos que va aconsultar la base de datos
        fields = ('id','nombre', 'precio', 'stock', 'imagen')

productSchema   = ProductSchema()
productsSchemas = ProductSchema(many=True)
