from flask import  Blueprint
from app.views.viewTalle import *
talle = Blueprint('talle', __name__)


talle.route('/api/talle/', methods=['GET'])(get_all_Talles)
talle.route('/api/talle/', methods=['POST'])(create_talle)
talle.route('/api/talle/<int:id>', methods=['DELETE'])(delete_talle)
talle.route('/api/talle/<int:id>', methods=['PUT'])(update_talle)