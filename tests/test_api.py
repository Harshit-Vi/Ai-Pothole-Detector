"""Test API endpoints."""
import pytest
from backend.app import create_app
from backend.database.db_init import db

@pytest.fixture
def app():
    """Create test app."""
    app = create_app('testing')
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()

class TestDetectAPI:
    """Test detection API endpoints."""
    
    def test_health_endpoint(self, client):
        """Test health check."""
        response = client.get('/health')
        assert response.status_code == 200
        assert response.json['status'] == 'healthy'
    
    def test_detect_image_endpoint(self, client):
        """Test detection endpoint."""
        # TODO: Add test image
        pass

class TestReportAPI:
    """Test report endpoints."""
    
    def test_get_reports(self, client):
        """Test get reports endpoint."""
        response = client.get('/api/reports')
        assert response.status_code == 200
        assert 'reports' in response.json
