"""Map generation and visualization service."""
from typing import List, Dict, Tuple
import folium
from backend.utils.logger import setup_logger

logger = setup_logger(__name__)

class MapService:
    """Service for map generation and visualization."""
    
    def __init__(self, center_lat: float = 28.7041, center_lon: float = 77.1025, zoom: int = 12):
        """Initialize map service.
        
        Args:
            center_lat: Center latitude (default: Delhi)
            center_lon: Center longitude
            zoom: Initial zoom level
        """
        self.center_lat = center_lat
        self.center_lon = center_lon
        self.zoom = zoom
    
    def create_map(self, pothole_data: List[Dict]) -> folium.Map:
        """Create a folium map with pothole markers.
        
        Args:
            pothole_data: List of pothole dictionaries with location and severity
            
        Returns:
            folium Map object
        """
        try:
            map_obj = folium.Map(
                location=[self.center_lat, self.center_lon],
                zoom_start=self.zoom,
                tiles='OpenStreetMap'
            )
            
            # Add pothole markers
            for pothole in pothole_data:
                latitude = pothole.get('latitude')
                longitude = pothole.get('longitude')
                severity = pothole.get('severity', 'unknown')
                
                if latitude and longitude:
                    # Color based on severity
                    color = self._get_color_by_severity(severity)
                    
                    folium.CircleMarker(
                        location=[latitude, longitude],
                        radius=8,
                        popup=f"Severity: {severity}",
                        color=color,
                        fill=True,
                        fillColor=color,
                        fillOpacity=0.7,
                        weight=2
                    ).add_to(map_obj)
            
            logger.info(f'Map created with {len(pothole_data)} markers')
            return map_obj
        except Exception as e:
            logger.error(f'Error creating map: {e}')
            return None
    
    def _get_color_by_severity(self, severity: str) -> str:
        """Get color code based on severity.
        
        Args:
            severity: Severity level
            
        Returns:
            Color code
        """
        colors = {
            'minor': 'yellow',
            'medium': 'orange',
            'severe': 'red'
        }
        return colors.get(severity, 'gray')
    
    def export_map(self, map_obj: folium.Map, filepath: str) -> bool:
        """Export map to HTML file.
        
        Args:
            map_obj: folium Map object
            filepath: Output file path
            
        Returns:
            True if successful
        """
        try:
            map_obj.save(filepath)
            logger.info(f'Map exported to {filepath}')
            return True
        except Exception as e:
            logger.error(f'Error exporting map: {e}')
            return False
