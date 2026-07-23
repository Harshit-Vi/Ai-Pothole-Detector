"""Database initialization."""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from backend.utils.logger import setup_logger

logger = setup_logger(__name__)

db = SQLAlchemy()
migrate = Migrate()

def init_db(app):
    """Initialize database.
    
    Args:
        app: Flask application instance
    """
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        try:
            db.create_all()
            logger.info('Database tables created successfully')
        except Exception as e:
            logger.error(f'Error creating database tables: {e}')
