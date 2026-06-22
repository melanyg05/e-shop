from flask import Blueprint

public_bp = Blueprint(
    'admin', 
    __name__, 
    template_folder='../../templates/admin'
    )

from . import routes