from flask import Flask
from flask_restful import Resource, Api, marshal_with, marshal
from models.Hotel import hotel_resource_fields, Hotel
from response import response_resource_fields, Response

#Routes imports
from services.router.HotelsRouter import MainRouter

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        hotel_resource_fields['nombre'] = 'pedro'
        hotel_resource_fields['nombre2'] = 'andreu'
        
        return hotel_resource_fields
api.add_resource(HelloWorld, '/')

class HelloWorldMarshal(Resource):
    @marshal_with(hotel_resource_fields)
    def get(self):
        return Hotel('prueba bunbury', 'cardiel')
api.add_resource(HelloWorldMarshal, '/marshal')

class TestResponse(Resource):
    @marshal_with(response_resource_fields)
    def get(self):
        return Response(0,'ha stato tutto benne!',  [ marshal(Hotel('prueba bunbury','cardiel'),hotel_resource_fields) ],  200)
api.add_resource(TestResponse, '/response')


MainRouter(api).init()

if __name__ == '__main__':
    app.run(debug=True)