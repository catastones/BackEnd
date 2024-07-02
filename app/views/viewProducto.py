from flask import jsonify, request
from app.models.productos import Producto

def index():
    response = {'message':'Hola mundo API FLASK 🐍'}
    return jsonify(response)

#funcion que busca todo el listado de los productos
def get_all_producto():
    productos = Producto.get_all()
    list_productos = [producto.serialize() for producto in productos]
    return jsonify(list_productos)

#funcion que busca todo el listado de los productos por genero
def get_producto_gen(id_genero):
    productos = Producto.get_by_gen(id_genero)
    list_productos = [producto.serialize() for producto in productos]
    return jsonify(list_productos)

#funcion que busca un Producto por id
def get_producto(id):
    producto = Producto.get_by_id(id)
    if not producto:
        return jsonify({'message': 'Producto not found'}), 404
    return jsonify(producto.serialize())
def create_producto():
    data = request.json
    print(data)
    #agregar una logica de validacion de datos
    new_producto = Producto(None,data['nombre'],data['descripcion'],data['id_talle'],data['id_color'],data['id_genero'],data['url_image'],data['price'])
    new_producto.save()
    return jsonify({'message':'Producto creado con exito'}), 201
    

def update_producto(id):
    producto = Producto.get_by_id(id)
    print(producto.id)
    if not producto:
        return jsonify({'message': 'Producto not found'}), 404
    data = request.json
   
    producto.nombre = data['nombre']
    producto.descripcion = data['descripcion']
    producto.id_talle = data['id_talle']
    producto.id_color = data['id_color']
    producto.id_genero = data['id_genero']
    producto.url_image = data['url_image']
    producto.price = data['price']
    producto.save()
    return jsonify({'message': 'producto updated successfully'})

def delete_producto(id):
    producto = Producto.get_by_id(id)
   
    if not producto:
        return jsonify({'message': 'Producto not found'}), 404
    producto.delete()
    return jsonify({'message': 'Producto deleted successfully'})