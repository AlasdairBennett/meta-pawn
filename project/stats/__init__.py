"""
The stats blueprint handles the main stats viewer of the application
"""
from flask import Blueprint

stats_blueprint = Blueprint('stats', __name__, template_folder='templates')

from . import routes
