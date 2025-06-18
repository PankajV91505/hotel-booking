# app/views/hotels.py

from flask import Blueprint, render_template, request, flash
from ..models import Hotel, db
from datetime import datetime
import random
import uuid

hotels_bp = Blueprint('hotels', __name__, url_prefix='/hotels')

# 🔧 Generate UUID manually (in case `generate_uuid` isn't imported)
def generate_uuid():
    return str(uuid.uuid4())

def generate_demo_hotels(n=200):
    names = ['Grand Palace', 'Royal Stay', 'Comfort Inn', 'Sea View', 'Mountain Lodge', 'Elite Retreat', 'Urban Nest', 'Sunrise Hotel']
    cities = ['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore', 'Pune', 'Jaipur', 'Lucknow']
    descriptions = [
        'Luxurious stay with top amenities.',
        'A perfect place for business and leisure.',
        'Cozy rooms with great city views.',
        'Beachside comfort with excellent service.',
        'Nestled in the mountains for a peaceful retreat.'
    ]
    
    hotels = []
    for i in range(n):
        hotel = Hotel(
            id=generate_uuid(),
            name=f"{random.choice(names)} #{i+1}",
            location=random.choice(cities),
            description=random.choice(descriptions),
            star_rating=random.randint(3, 5),
            created_at=datetime.utcnow()
        )
        db.session.add(hotel)
        hotels.append(hotel)
    db.session.commit()
    return hotels

@hotels_bp.route('/')
@hotels_bp.route('/list')
def list_hotels():
    search_query = request.args.get('q', '').strip()
    
    # Insert demo hotels only if DB is empty
    hotels = Hotel.query.all()
    if not hotels:
        hotels = generate_demo_hotels()

    # Filter by name or location
    if search_query:
        hotels = Hotel.query.filter(
            (Hotel.name.ilike(f"%{search_query}%")) |
            (Hotel.location.ilike(f"%{search_query}%"))
        ).all()
        if not hotels:
            flash(f'No hotels found for "{search_query}".')

    return render_template('hotels/list.html', hotels=hotels, query=search_query)

@hotels_bp.route('/<string:hotel_id>')
def hotel_detail(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    return render_template('hotels/detail.html', hotel=hotel)
