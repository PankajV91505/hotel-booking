# File: app/views/home.py
from flask import Blueprint, render_template
from app.models import Hotel

home_bp = Blueprint('home', __name__)

# # @home_bp.route('/')
# # def index():
# #     return """
# #     <h1>Welcome to the Hotel Booking App</h1>
# #     <p><a href='/hotels'>View Hotels</a></p>
# #     <p><a href='/dashboard'>Go to Dashboard</a></p>
# #     """
@home_bp.route('/')
def home():
    hotels = Hotel.query.limit(6).all()  # Show top 6
    return render_template("home.html", hotels=hotels)