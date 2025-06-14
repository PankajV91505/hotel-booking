# File: app/views/home.py
from flask import Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    return """
    <h1>Welcome to the Hotel Booking App</h1>
    <p><a href='/hotels'>View Hotels</a></p>
    <p><a href='/dashboard'>Go to Dashboard</a></p>
    """
