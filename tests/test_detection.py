"""Test detection model."""
import pytest
from backend.models.pothole_detector import PotholeDetector
from backend.models.severity_classifier import SeverityClassifier
import numpy as np
import cv2

class TestPotholeDetector:
    """Test pothole detection."""
    
    @pytest.fixture
    def detector(self):
        """Initialize detector."""
        return PotholeDetector('./models/trained_model.pt')
    
    def test_detector_initialization(self, detector):
        """Test detector initialization."""
        assert detector.model is not None
        assert detector.confidence_threshold == 0.5
    
    def test_detection_on_image(self, detector):
        """Test detection on sample image."""
        # Create dummy image
        image = np.random.randint(0, 255, (640, 480, 3), dtype=np.uint8)
        result = detector.detect(image)
        
        assert result['success'] is True
        assert 'detections' in result
        assert 'image_shape' in result

class TestSeverityClassifier:
    """Test severity classification."""
    
    @pytest.fixture
    def classifier(self):
        """Initialize classifier."""
        return SeverityClassifier()
    
    def test_minor_severity(self, classifier):
        """Test minor severity classification."""
        detection = {
            'bbox': {'width': 50, 'height': 50},
            'confidence': 0.7
        }
        result = classifier.classify(detection)
        assert result['severity'] == 'minor'
    
    def test_severe_severity(self, classifier):
        """Test severe severity classification."""
        detection = {
            'bbox': {'width': 300, 'height': 300},
            'confidence': 0.9
        }
        result = classifier.classify(detection)
        assert result['severity'] == 'severe'
