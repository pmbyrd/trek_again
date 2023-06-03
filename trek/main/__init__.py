"""
This files initializes the main package.
Handles routes that do not need authentication throughout the application.
"""

from flask import Blueprint

main = Blueprint('main', __name__)

#NOTE: Import any endpoints here to avoid circular imports.
from main import routes