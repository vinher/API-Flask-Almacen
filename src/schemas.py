from flask_marshmallow import Marshmallow

ma = Marshmallow()

class ProductSchema(ma.Schema):
    class Meta:
        #Campos que va aconsultar la base de datos
        fields = ('id','nombre', 'precio', 'stock', 'image')

productSchema   = ProductSchema()
productsSchemas = ProductSchema(many=True)



class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre_usuario', 'contrasena', 'token_sesion', 'fecha_creacion','fecha_actualizacion')


userSchema = UserSchema()
usersSchema = UserSchema(many=True)