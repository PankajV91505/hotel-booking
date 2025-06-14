# app/views/hotels.py

from flask import Blueprint, render_template, request
from ..models import Hotel

hotels_bp = Blueprint('hotels', __name__, url_prefix='/hotels')

@hotels_bp.route('/')
def list_hotels():
    hotels = Hotel.query.all()
    return render_template('hotels/list.html', hotels=hotels)
