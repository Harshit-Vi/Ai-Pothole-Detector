"""Image processing utilities."""
import cv2
import numpy as np
import requests
from io import BytesIO
from backend.utils.logger import setup_logger

logger = setup_logger(__name__)

def process_image(source, max_width=1280, max_height=720):
    """Process image from URL or file.
    
    Args:
        source: Image URL or file path
        max_width: Maximum width for resizing
        max_height: Maximum height for resizing
        
    Returns:
        Processed image as numpy array or None
    """
    try:
        if isinstance(source, str):
            if source.startswith('http'):
                # Load from URL
                response = requests.get(source, timeout=10)
                image_data = np.frombuffer(response.content, np.uint8)
                image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
            else:
                # Load from file
                image = cv2.imread(source)
        else:
            image = source
        
        if image is None:
            logger.error('Failed to load image')
            return None
        
        # Resize if necessary
        height, width = image.shape[:2]
        if width > max_width or height > max_height:
            scale = min(max_width / width, max_height / height)
            new_width = int(width * scale)
            new_height = int(height * scale)
            image = cv2.resize(image, (new_width, new_height))
        
        return image
    except Exception as e:
        logger.error(f'Error processing image: {e}')
        return None

def resize_image(image, width, height):
    """Resize image to specified dimensions.
    
    Args:
        image: Input image
        width: Target width
        height: Target height
        
    Returns:
        Resized image
    """
    return cv2.resize(image, (width, height))

def normalize_image(image):
    """Normalize image values to 0-1 range.
    
    Args:
        image: Input image
        
    Returns:
        Normalized image
    """
    return image.astype(np.float32) / 255.0
