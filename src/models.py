from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    id      = db.Column(db.Integer      , primary_key=True)
    nombre  = db.Column(db.String(100)  , nullable=False)
    precio  = db.Column(db.Float        , nullable=False)
    stock   = db.Column(db.Integer      , nullable=False)
    image   = db.Column(db.String(255)  , nullable=False)

    def __init__(self, nombre, precio, stock, image):
        self.nombre = nombre
        self.precio = precio
        self.stock  = stock
        self.image  = image



class Users(db.Model):
        id                  = db.Column(db.Integer      , primary_key=True)
        nombre_usuario      = db.Column(db.String(100)  , nullable=False, unique=True)
        contrasena          = db.Column(db.String(100)  , nullable=False)
        token_sesion        = db.Column(db.String(100)  , nullable=False)
        fecha_creacion      = db.Column(db.String(100)  , nullable=False)
        fecha_actualizacion = db.Column(db.String(255)  , nullable=False)

        def __init__(self, nombre_usuario, contrasena, token_sesion, fecha_creacion, fecha_actualizacion):
            self.nombre_usuario      = nombre_usuario
            self.contrasena          = contrasena
            self.token_sesion        = token_sesion
            self.fecha_creacion      = fecha_creacion
            self.fecha_actualizacion = fecha_actualizacion