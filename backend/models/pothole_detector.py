"""YOLOv8 pothole detection model wrapper."""
import cv2
import numpy as np
from ultralytics import YOLO
from typing import Tuple, List, Dict
import os
from backend.utils.logger import setup_logger

logger = setup_logger(__name__)

class PotholeDetector:
    """Wrapper for YOLOv8 model for pothole detection."""
    
    def __init__(self, model_path: str, confidence_threshold: float = 0.5, iou_threshold: float = 0.4):
        """Initialize the pothole detector.
        
        Args:
            model_path: Path to the trained YOLOv8 model
            confidence_threshold: Minimum confidence score for detections
            iou_threshold: IoU threshold for NMS
        """
        self.model_path = model_path
        self.confidence_threshold = confidence_threshold
        self.iou_threshold = iou_threshold
        self.model = None
        self._load_model()
    
    def _load_model(self):
        """Load the YOLOv8 model."""
        try:
            if os.path.exists(self.model_path):
                self.model = YOLO(self.model_path)
                logger.info(f'Model loaded successfully from {self.model_path}')
            else:
                # Download pretrained model if not found
                logger.warning(f'Model not found at {self.model_path}. Loading pretrained YOLOv8n...')
                self.model = YOLO('yolov8n.pt')
        except Exception as e:
            logger.error(f'Error loading model: {e}')
            raise
    
    def detect(self, image: np.ndarray) -> Dict:
        """Detect potholes in an image.
        
        Args:
            image: Input image as numpy array (BGR format)
            
        Returns:
            Dictionary containing detection results
        """
        try:
            if self.model is None:
                raise RuntimeError('Model not loaded')
            
            # Run inference
            results = self.model(
                image,
                conf=self.confidence_threshold,
                iou=self.iou_threshold,
                verbose=False
            )
            
            detections = []
            if results and len(results) > 0:
                result = results[0]
                if result.boxes is not None:
                    for box in result.boxes:
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        conf = float(box.conf[0].cpu().numpy())
                        
                        detection = {
                            'bbox': {
                                'x1': float(x1),
                                'y1': float(y1),
                                'x2': float(x2),
                                'y2': float(y2),
                                'width': float(x2 - x1),
                                'height': float(y2 - y1)
                            },
                            'confidence': conf
                        }
                        detections.append(detection)
            
            return {
                'detections': detections,
                'image_shape': image.shape,
                'success': True
            }
        except Exception as e:
            logger.error(f'Error during detection: {e}')
            return {
                'detections': [],
                'error': str(e),
                'success': False
            }
    
    def detect_from_file(self, image_path: str) -> Dict:
        """Detect potholes from an image file.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Dictionary containing detection results
        """
        try:
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError(f'Failed to read image from {image_path}')
            
            return self.detect(image)
        except Exception as e:
            logger.error(f'Error detecting from file: {e}')
            return {
                'detections': [],
                'error': str(e),
                'success': False
            }
