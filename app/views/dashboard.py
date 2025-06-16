# File: app/views/dashboard.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models import User, Hotel, Room

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        users = User.query.all()
        hotels = Hotel.query.all()
        rooms = Room.query.all()
        return render_template('dashboard/admin_dashboard.html', users=users, hotels=hotels, rooms=rooms)
    return render_template('dashboard/user_dashboard.html', user=current_user) 

