from flask import jsonify, request
from app.models.generos import Generos


#funcion que busca todo el listado de las Generos
def get_all_Generos():
    generos = Generos.get_all()
    list_generos = [genero.serialize() for genero in generos]
    return jsonify(list_generos)


def create_genero():
    data = request.json
    #agregar una logica de validacion de datos
    new_genero = Generos(None,data['genero'])
    new_genero.save()
    return jsonify({'message':'Genero creado con exito'}), 201
    

def update_genero(id):
    genero = Generos.get_by_id(id)
    if not genero:
        return jsonify({'message': 'Genero not found'}), 404
    data = request.json
    genero.genero = data['genero']   
    genero.save()
    return jsonify({'message': 'Genero updated successfully'})

def delete_genero(id):
    genero = Generos.get_by_id(id)
    if not genero:
        return jsonify({'message': 'Genero not found'}), 404
    genero.delete()
    return jsonify({'message': 'Genero deleted successfully'})