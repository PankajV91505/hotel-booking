# File: app/views/rooms.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from ..models import Room, Hotel, db

rooms_bp = Blueprint('rooms', __name__, url_prefix='/rooms')

@rooms_bp.route('/<hotel_id>')
def list_rooms(hotel_id):
    rooms = Room.query.filter_by(hotel_id=hotel_id, is_available=True).all()
    return render_template('rooms/list.html', rooms=rooms)

@rooms_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create_room():
    if current_user.role != 'admin':
        return redirect(url_for('dashboard.dashboard'))
    if request.method == 'POST':
        room = Room(
            hotel_id=request.form['hotel_id'],
            room_type=request.form['room_type'],
            price_per_night=request.form['price_per_night'],
            max_guests=request.form['max_guests'],
            amenities=request.form['amenities']
        )
        db.session.add(room)
        db.session.commit()
        flash('Room added.')
        return redirect(url_for('dashboard.dashboard'))
    hotels = Hotel.query.all()
    return render_template('rooms/create.html', hotels=hotels)

@rooms_bp.route('/<room_id>/delete')
@login_required
def delete_room(room_id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard.dashboard'))
    room = Room.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    flash('Room deleted.')
    return redirect(url_for('dashboard.dashboard'))

@rooms_bp.route('/<room_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_room(room_id):
    if current_user.role != 'admin':
        return redirect(url_for('dashboard.dashboard'))
    room = Room.query.get_or_404(room_id)
    if request.method == 'POST':
        room.room_type = request.form['room_type']
        room.price_per_night = request.form['price_per_night']
        room.max_guests = request.form['max_guests']
        room.amenities = request.form['amenities']
        db.session.commit()
        flash('Room updated.')
        return redirect(url_for('dashboard.dashboard'))
    return render_template('rooms/edit.html', room=room)
