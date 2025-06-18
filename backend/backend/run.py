## Phase 1, 2, 3, 4, 5, 6, 7 & 8: Flask Hotel Booking App (Full Feature Set)

# Folder: hotel-booking/
# File: run.py

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)








# Templating: Add `rooms/list.html`, `rooms/create.html`, `rooms/edit.html`, `dashboard/admin_dashboard.html`
# Booking form with hidden inputs (room_id, check_in, check_out) submits to `/bookings/create/<room_id>`

# Update templates:
# In `dashboard/user_dashboard.html` and `dashboard/admin_dashboard.html` add:
# <p><a href="{{ url_for('bookings.booking_history') }}">View Booking History</a></p>
