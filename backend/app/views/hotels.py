# app/views/hotels.py

from flask import Blueprint, render_template, request, flash
from ..models import Hotel

hotels_bp = Blueprint('hotels', __name__, url_prefix='/hotels')


@hotels_bp.route('/')
@hotels_bp.route('/list')  # ✅ now both /hotels/ and /hotels/list will work
def list_hotels():
    search_query = request.args.get('q', '').strip()
    hotels = []

    if search_query:
        hotels = Hotel.query.filter(
            (Hotel.name.ilike(f"%{search_query}%")) |
            (Hotel.city.ilike(f"%{search_query}%"))
        ).all()
        if not hotels:
            flash(f'No hotels found for "{search_query}".')
    else:
        hotels = Hotel.query.all()

    return render_template('hotels/list.html', hotels=hotels, query=search_query)

@hotels_bp.route('/<int:hotel_id>')
def hotel_detail(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    return render_template('hotels/detail.html', hotel=hotel)
