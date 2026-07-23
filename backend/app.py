"""Main Flask application entry point."""
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os
from backend.config import config
from backend.database.db_init import init_db
from backend.routes import detect, reports, dashboard
from backend.utils.logger import setup_logger

# Load environment variables
load_dotenv()

# Initialize logger
logger = setup_logger(__name__)

def create_app(config_name=None):
    """Application factory function.
    
    Args:
        config_name: Configuration environment (development, production, testing)
        
    Returns:
        Flask application instance
    """
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Enable CORS
    CORS(app)
    
    # Initialize database
    init_db(app)
    
    # Register blueprints
    app.register_blueprint(detect.detect_bp)
    app.register_blueprint(reports.reports_bp)
    app.register_blueprint(dashboard.dashboard_bp)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Resource not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        logger.error(f'Internal server error: {error}')
        return {'error': 'Internal server error'}, 500
    
    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health_check():
        return {'status': 'healthy'}, 200
    
    logger.info('Flask application created successfully')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        host=os.getenv('API_HOST', '0.0.0.0'),
        port=int(os.getenv('API_PORT', 5000)),
        debug=os.getenv('DEBUG', False)
    )
