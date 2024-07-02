from flask import Flask,Blueprint
from app.database import init_app
from app.routes.routesColores import color
from app.routes.routesTalles import talle
from app.routes.routesGeneros import genero
from app.routes.routesProductos import producto


from flask_cors import CORS

#Crear una instancia de Flask
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})
#asociacion de rutas con vistas
app.register_blueprint(color)
app.register_blueprint(talle)
app.register_blueprint(genero)
app.register_blueprint(producto)

init_app(app)
#permita solicitudes desde cualquier origen

#/CORS(app)


#Permite separa el codigo que se ejecuta cuando se corre el archivo
if __name__=='__main__':
    app.run(debug=True)