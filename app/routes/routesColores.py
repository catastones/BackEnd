from flask import  Blueprint
from app.views.viewColor import *
color = Blueprint('color', __name__)


color.route('/api/color/', methods=['GET'])(get_all_colores)
color.route('/api/color/', methods=['POST'])(create_color)
color.route('/api/color/<int:id>', methods=['DELETE'])(delete_color)
color.route('/api/colores/<int:id>', methods=['PUT'])(update_color)