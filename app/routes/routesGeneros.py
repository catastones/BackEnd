from flask import  Blueprint
from app.views.viewGenero import *
genero = Blueprint('genero', __name__)


genero.route('/api/genero/', methods=['GET'])(get_all_Generos)
genero.route('/api/genero/', methods=['POST'])(create_genero)
genero.route('/api/genero/<int:id>', methods=['DELETE'])(delete_genero)
genero.route('/api/genero/<int:id>', methods=['PUT'])(update_genero)