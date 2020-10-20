from flask_restful import fields

hotel_resource_fields = {
    'nombre': fields.String,
    'nombre2': fields.String,
}

class Hotel(object):
    def __init__(self, nombre, nombre2):
        self.nombre = nombre
        self.nombre2 = nombre2
