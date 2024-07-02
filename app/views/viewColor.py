from flask import jsonify, request
from app.models.colores import Colores


#funcion que busca todo el listado de las colores
def get_all_colores():
    colores = Colores.get_all()
    list_colores = [color.serialize() for color in colores]
    return jsonify(list_colores)




def create_color():
    data = request.json
    #agregar una logica de validacion de datos
    new_color = Colores(None,data['color'])
    new_color.save()
    return jsonify({'message':'Color creado con exito'}), 201
    

def update_color(id):
    color = Colores.get_by_id(id)
    if not color:
        return jsonify({'message': 'Color not found'}), 404
    data = request.json
    color.color = data['color']   
    color.save()
    return jsonify({'message': 'Color updated successfully'})

def delete_color(id):
    color = Colores.get_by_id(id)
    if not color:
        return jsonify({'message': 'Color not found'}), 404
    color.delete()
    return jsonify({'message': 'Color deleted successfully'})