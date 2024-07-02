from flask import  Blueprint
from app.views.viewProducto import *
producto = Blueprint('producto', __name__)

producto.route('/', methods=['GET'])(index)
producto.route('/api/producto/', methods=['GET'])(get_all_producto)
producto.route('/api/producto/<int:id>', methods=['GET'])(get_producto)
producto.route('/api/producto/genero/<int:id_genero>', methods=['GET'])(get_producto_gen)
producto.route('/api/producto/', methods=['POST'])(create_producto)
producto.route('/api/producto/<int:id>', methods=['PUT'])(update_producto)
producto.route('/api/producto/<int:id>', methods=['DELETE'])(delete_producto)