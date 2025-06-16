# File: app/views/bookings.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime
from ..models import Booking, Room, db

bookings_bp = Blueprint('bookings', __name__, url_prefix='/bookings')

@bookings_bp.route('/create/<room_id>', methods=['POST'])
@login_required
def book_room(room_id):
    check_in = datetime.strptime(request.form['check_in'], '%Y-%m-%d')
    check_out = datetime.strptime(request.form['check_out'], '%Y-%m-%d')
    room = Room.query.get(room_id)

    nights = (check_out - check_in).days
    total_price = nights * room.price_per_night

    booking = Booking(
        user_id=current_user.id,
        hotel_id=room.hotel_id,
        room_id=room.id,
        check_in=check_in,
        check_out=check_out,
        total_price=total_price
    )
    room.is_available = False
    db.session.add(booking)
    db.session.commit()
    flash('Room booked successfully.')
    return redirect(url_for('hotels.list_hotels'))

@bookings_bp.route('/history')
@login_required
def booking_history():
    if current_user.role == 'admin':
        bookings = Booking.query.all()
    else:
        bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('bookings/history.html', bookings=bookings)

@bookings_bp.route('/<booking_id>/cancel')
@login_required
def cancel_booking(booking_id):
    booking = Booking.query.get_or_404(booking_id)

    if current_user.role != 'admin' and booking.user_id != current_user.id:
        flash("Unauthorized access.")
        return redirect(url_for('bookings.booking_history'))

    booking.status = 'cancelled'
    room = Room.query.get(booking.room_id)
    room.is_available = True

    db.session.commit()
    flash('Booking cancelled successfully.')
    return redirect(url_for('bookings.booking_history'))
