"""Severity classification for detected potholes."""
from typing import Dict
from backend.utils.logger import setup_logger

logger = setup_logger(__name__)

class SeverityClassifier:
    """Classify pothole severity based on detection metrics."""
    
    # Severity levels
    SEVERITY_MINOR = 'minor'
    SEVERITY_MEDIUM = 'medium'
    SEVERITY_SEVERE = 'severe'
    
    # Size thresholds (in pixels)
    MINOR_MAX_AREA = 5000      # < 5000 sq pixels
    MEDIUM_MAX_AREA = 20000    # < 20000 sq pixels
    
    def __init__(self):
        """Initialize severity classifier."""
        self.thresholds = {
            'minor': {'area': self.MINOR_MAX_AREA, 'confidence': 0.5},
            'medium': {'area': self.MEDIUM_MAX_AREA, 'confidence': 0.6},
            'severe': {'area': float('inf'), 'confidence': 0.7}
        }
    
    def classify(self, detection: Dict) -> Dict:
        """Classify severity of a pothole detection.
        
        Args:
            detection: Detection dictionary with bbox and confidence
            
        Returns:
            Dictionary with severity classification and score
        """
        try:
            bbox = detection.get('bbox', {})
            confidence = detection.get('confidence', 0.0)
            
            # Calculate area
            width = bbox.get('width', 0)
            height = bbox.get('height', 0)
            area = width * height
            
            # Classify based on area and confidence
            severity = self._classify_by_area(area)
            
            # Adjust based on confidence
            confidence_factor = min(confidence / 0.9, 1.0)  # Normalize confidence
            
            # Calculate severity score (0-1)
            severity_score = self._calculate_severity_score(area, confidence)
            
            return {
                'severity': severity,
                'severity_score': severity_score,
                'area': area,
                'confidence': confidence,
                'confidence_factor': confidence_factor
            }
        except Exception as e:
            logger.error(f'Error classifying severity: {e}')
            return {
                'severity': self.SEVERITY_MINOR,
                'severity_score': 0.3,
                'error': str(e)
            }
    
    def _classify_by_area(self, area: float) -> str:
        """Classify severity by area.
        
        Args:
            area: Bounding box area in pixels
            
        Returns:
            Severity level string
        """
        if area < self.MINOR_MAX_AREA:
            return self.SEVERITY_MINOR
        elif area < self.MEDIUM_MAX_AREA:
            return self.SEVERITY_MEDIUM
        else:
            return self.SEVERITY_SEVERE
    
    def _calculate_severity_score(self, area: float, confidence: float) -> float:
        """Calculate a severity score (0-1).
        
        Args:
            area: Bounding box area in pixels
            confidence: Model confidence score
            
        Returns:
            Severity score between 0 and 1
        """
        # Area-based component (0-0.6)
        area_score = min(area / self.MEDIUM_MAX_AREA, 1.0) * 0.6
        
        # Confidence-based component (0-0.4)
        confidence_score = confidence * 0.4
        
        return area_score + confidence_score
