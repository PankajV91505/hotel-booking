# File: app/models.py
from . import db, login_manager
from flask_login import UserMixin
from datetime import datetime
import uuid

def generate_uuid():
    return str(uuid.uuid4())

# ---------------------- User Model ----------------------
class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), default='user')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    bookings = db.relationship('Booking', backref='user', lazy=True)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# ---------------------- Hotel Model ----------------------
class Hotel(db.Model):
    __tablename__ = 'hotel'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    star_rating = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    rooms = db.relationship('Room', backref='hotel', lazy=True)
    bookings = db.relationship('Booking', backref='hotel', lazy=True)

# ---------------------- Room Model ----------------------
class Room(db.Model):
    __tablename__ = 'room'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    hotel_id = db.Column(db.String, db.ForeignKey('hotel.id'), nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)
    amenities = db.Column(db.String)
    is_available = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    bookings = db.relationship('Booking', backref='room', lazy=True)

# ---------------------- Booking Model ----------------------
class Booking(db.Model):
    __tablename__ = 'booking'

    id = db.Column(db.String, primary_key=True, default=generate_uuid)
    user_id = db.Column(db.String, db.ForeignKey('user.id'), nullable=False)
    hotel_id = db.Column(db.String, db.ForeignKey('hotel.id'), nullable=False)
    room_id = db.Column(db.String, db.ForeignKey('room.id'), nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='confirmed')
    total_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
