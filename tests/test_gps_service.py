"""Test GPS service."""
import pytest
from backend.services.gps_service import GPSService

class TestGPSService:
    """Test GPS functionality."""
    
    @pytest.fixture
    def gps_service(self):
        """Initialize GPS service."""
        return GPSService()
    
    def test_get_address_from_coordinates(self, gps_service):
        """Test getting address from coordinates."""
        lat, lon = 28.7041, 77.1025
        address = gps_service.get_address_from_coordinates(lat, lon)
        assert address is not None
        assert isinstance(address, str)
    
    def test_calculate_distance(self, gps_service):
        """Test distance calculation."""
        distance = gps_service.calculate_distance(28.7041, 77.1025, 28.7050, 77.1030)
        assert distance > 0
        assert isinstance(distance, float)
