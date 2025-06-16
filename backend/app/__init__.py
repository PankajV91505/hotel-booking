# File: app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Fallback secret key if not defined in config
    if not app.config.get('SECRET_KEY'):
        app.config['SECRET_KEY'] = 'supersecretkey'

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Flask-Login config
    login_manager.login_view = 'auth.login'  # where to redirect when not logged in
    login_manager.login_message_category = 'warning'

    # Import models
    from .models import User

    # Flask-Login user loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # Register blueprints
    from .views.home import home_bp
    from .views.auth import auth_bp
    from .views.hotels import hotels_bp
    from .views.rooms import rooms_bp
    from .views.bookings import bookings_bp
    from .views.dashboard import dashboard_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(hotels_bp)
    app.register_blueprint(rooms_bp)
    app.register_blueprint(bookings_bp)  # ✅ use only this one
    app.register_blueprint(dashboard_bp)

    return app
