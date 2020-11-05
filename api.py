import os
from flask import Flask
from flask_restful import Resource, Api, marshal_with, marshal
from models.Hotel import hotel_resource_fields, Hotel
from response import response_resource_fields, Response

#Routes imports
from services.router.HotelsRouter import MainRouter as HotelsMainRouter
from services.router.ReviewsRouter import MainRouter as ReviewsMainRouter

port = int(os.environ.get("PORT", 5000))

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        
        hotel_resource_fields['nombre'] = 'pedro'
        hotel_resource_fields['nombre2'] = 'andreu'
        
        return hotel_resource_fields
api.add_resource(HelloWorld, '/hello')

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

class Main(Resource):
    @marshal_with(response_resource_fields)
    def get(self):
        return Response(0,'Bienvenido a la API de análisis de reviews en su versión local!',  None,  200)
api.add_resource(Main, '/')


HotelsMainRouter(api).init()
ReviewsMainRouter(api).init()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=port)