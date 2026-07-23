"""GPS location tagging service."""
from typing import Dict, Tuple
from geopy.geocoders import Nominatim
from backend.utils.logger import setup_logger

logger = setup_logger(__name__)

class GPSService:
    """Service for GPS location tagging and geocoding."""
    
    def __init__(self):
        """Initialize GPS service."""
        self.geocoder = Nominatim(user_agent='pothole_detector')
    
    def get_address_from_coordinates(self, latitude: float, longitude: float) -> str:
        """Get address from GPS coordinates.
        
        Args:
            latitude: Latitude coordinate
            longitude: Longitude coordinate
            
        Returns:
            Address string
        """
        try:
            location = self.geocoder.reverse(f"{latitude}, {longitude}")
            return location.address
        except Exception as e:
            logger.error(f'Error getting address: {e}')
            return f"{latitude}, {longitude}"
    
    def get_coordinates_from_address(self, address: str) -> Tuple[float, float]:
        """Get GPS coordinates from address.
        
        Args:
            address: Address string
            
        Returns:
            Tuple of (latitude, longitude)
        """
        try:
            location = self.geocoder.geocode(address)
            if location:
                return location.latitude, location.longitude
            return None, None
        except Exception as e:
            logger.error(f'Error getting coordinates: {e}')
            return None, None
    
    def calculate_distance(self, lat1: float, lon1: float, lat2: float, lon2: float) -> float:
        """Calculate distance between two coordinates using Haversine formula.
        
        Args:
            lat1, lon1: First coordinate
            lat2, lon2: Second coordinate
            
        Returns:
            Distance in kilometers
        """
        from math import radians, cos, sin, asin, sqrt
        
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371
        return c * r
