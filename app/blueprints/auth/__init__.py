from flask import Blueprint

public_bp = Blueprint(
    'auth', 
    __name__, 
    template_folder='../../templates/auth'
    )

from . import routes