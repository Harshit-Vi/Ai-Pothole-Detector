"""Input validation utilities."""
from typing import Tuple
import re

def validate_coordinates(latitude: float, longitude: float) -> bool:
    """Validate GPS coordinates.
    
    Args:
        latitude: Latitude value
        longitude: Longitude value
        
    Returns:
        True if valid
    """
    try:
        lat = float(latitude)
        lon = float(longitude)
        return -90 <= lat <= 90 and -180 <= lon <= 180
    except (ValueError, TypeError):
        return False

def validate_email(email: str) -> bool:
    """Validate email address.
    
    Args:
        email: Email address
        
    Returns:
        True if valid
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone: str) -> bool:
    """Validate phone number.
    
    Args:
        phone: Phone number
        
    Returns:
        True if valid
    """
    pattern = r'^\+?[1-9]\d{1,14}$'
    return re.match(pattern, phone.replace(' ', '')) is not None

def validate_severity(severity: str) -> bool:
    """Validate severity level.
    
    Args:
        severity: Severity level
        
    Returns:
        True if valid
    """
    return severity in ['minor', 'medium', 'severe']
