"""Detection endpoints for pothole detection."""
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
from backend.models.pothole_detector import PotholeDetector
from backend.models.severity_classifier import SeverityClassifier
from backend.utils.image_processor import process_image
from backend.utils.logger import setup_logger

logger = setup_logger(__name__)

detect_bp = Blueprint('detect', __name__, url_prefix='/api/detect')

# Initialize models
detector = None
classifier = None

def init_models():
    """Initialize detection models."""
    global detector, classifier
    if detector is None:
        detector = PotholeDetector(
            model_path=current_app.config['MODEL_PATH'],
            confidence_threshold=current_app.config['CONFIDENCE_THRESHOLD'],
            iou_threshold=current_app.config['IOU_THRESHOLD']
        )
    if classifier is None:
        classifier = SeverityClassifier()

@detect_bp.route('/image', methods=['POST'])
def detect_image():
    """Detect potholes in an uploaded image.
    
    Returns:
        JSON with detection results
    """
    try:
        init_models()
        
        # Check if image is in request
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Read image
        image_data = file.read()
        nparr = np.frombuffer(image_data, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            return jsonify({'error': 'Failed to decode image'}), 400
        
        # Detect potholes
        detection_result = detector.detect(image)
        
        if not detection_result['success']:
            return jsonify(detection_result), 400
        
        # Classify severity for each detection
        for detection in detection_result['detections']:
            severity_result = classifier.classify(detection)
            detection.update(severity_result)
        
        return jsonify(detection_result), 200
    
    except Exception as e:
        logger.error(f'Error in detect_image: {e}')
        return jsonify({'error': str(e)}), 500

@detect_bp.route('/url', methods=['POST'])
def detect_from_url():
    """Detect potholes from an image URL.
    
    Returns:
        JSON with detection results
    """
    try:
        init_models()
        
        data = request.get_json()
        image_url = data.get('image_url')
        
        if not image_url:
            return jsonify({'error': 'No image URL provided'}), 400
        
        # Download and process image
        image = process_image(image_url)
        if image is None:
            return jsonify({'error': 'Failed to process image'}), 400
        
        # Detect potholes
        detection_result = detector.detect(image)
        
        if not detection_result['success']:
            return jsonify(detection_result), 400
        
        # Classify severity
        for detection in detection_result['detections']:
            severity_result = classifier.classify(detection)
            detection.update(severity_result)
        
        return jsonify(detection_result), 200
    
    except Exception as e:
        logger.error(f'Error in detect_from_url: {e}')
        return jsonify({'error': str(e)}), 500

@detect_bp.route('/batch', methods=['POST'])
def detect_batch():
    """Detect potholes in multiple images.
    
    Returns:
        JSON with batch detection results
    """
    try:
        init_models()
        
        if 'images' not in request.files:
            return jsonify({'error': 'No images provided'}), 400
        
        files = request.files.getlist('images')
        results = []
        
        for file in files:
            if file.filename == '':
                continue
            
            image_data = file.read()
            nparr = np.frombuffer(image_data, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if image is not None:
                detection_result = detector.detect(image)
                
                if detection_result['success']:
                    for detection in detection_result['detections']:
                        severity_result = classifier.classify(detection)
                        detection.update(severity_result)
                
                results.append({
                    'filename': file.filename,
                    'result': detection_result
                })
        
        return jsonify({'batch_results': results, 'total': len(results)}), 200
    
    except Exception as e:
        logger.error(f'Error in detect_batch: {e}')
        return jsonify({'error': str(e)}), 500
