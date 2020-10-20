from flask_restful import fields

response_resource_fields = {
    'error': fields.String,
    'flash': fields.String,
    'data': fields.List(fields.Raw),
    'status': fields.Integer,
}

class Response(object):
    def __init__(self, error, flash, data, status):
        self.error = error
        self.flash = flash
        self.data = data
        self.status = status