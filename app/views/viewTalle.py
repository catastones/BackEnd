from flask import jsonify, request
from app.models.talles import Talles


#funcion que busca todo el listado de las Talles
def get_all_Talles():
    talles = Talles.get_all()
    list_talles = [talle.serialize() for talle in talles]
    return jsonify(list_talles)


def create_talle():
    data = request.json
    #agregar una logica de validacion de datos
    new_talle = Talles(None,data['talle'])
    new_talle.save()
    return jsonify({'message':'Talle creado con exito'}), 201
    

def update_talle(id):
    talle = Talles.get_by_id(id)
    if not talle:
        return jsonify({'message': 'Talle not found'}), 404
    data = request.json
    talle.talle = data['talle']   
    talle.save()
    return jsonify({'message': 'Talle updated successfully'})

def delete_talle(id):
    talle = Talles.get_by_id(id)
    if not talle:
        return jsonify({'message': 'talle not found'}), 404
    talle.delete()
    return jsonify({'message': 'Talle deleted successfully'})