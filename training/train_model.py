"""Train YOLOv8 model for pothole detection."""
import os
from ultralytics import YOLO
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PotholeModelTrainer:
    """Train YOLOv8 for pothole detection."""
    
    def __init__(self, model_name='yolov8n.pt', epochs=100, batch_size=32):
        """Initialize trainer.
        
        Args:
            model_name: YOLOv8 model size (yolov8n, yolov8s, yolov8m, yolov8l)
            epochs: Number of training epochs
            batch_size: Batch size for training
        """
        self.model_name = model_name
        self.epochs = epochs
        self.batch_size = batch_size
        self.model = None
    
    def load_model(self):
        """Load pretrained model."""
        logger.info(f"Loading {self.model_name}...")
        self.model = YOLO(self.model_name)
    
    def train(self, data_yaml='./datasets/data.yaml'):
        """Train the model.
        
        Args:
            data_yaml: Path to data.yaml file with dataset configuration
        """
        if self.model is None:
            self.load_model()
        
        logger.info(f"Starting training...")
        results = self.model.train(
            data=data_yaml,
            epochs=self.epochs,
            imgsz=640,
            batch=self.batch_size,
            patience=20,
            device=0,  # GPU device
            project='./runs/detect',
            name='pothole_detector',
            pretrained=True,
            cache=True,
            close_mosaic=10
        )
        
        logger.info(f"Training completed. Results: {results}")
        return results
    
    def evaluate(self, data_yaml='./datasets/data.yaml'):
        """Evaluate the model.
        
        Args:
            data_yaml: Path to data.yaml file
        """
        if self.model is None:
            self.load_model()
        
        logger.info("Starting evaluation...")
        metrics = self.model.val(data=data_yaml)
        logger.info(f"Evaluation completed. Metrics: {metrics}")
        return metrics
    
    def export_model(self, format='pt'):
        """Export trained model.
        
        Args:
            format: Export format (pt, onnx, tflite, pb)
        """
        if self.model is None:
            logger.error("No model loaded")
            return
        
        logger.info(f"Exporting model to {format}...")
        self.model.export(format=format)
        logger.info(f"Model exported successfully")

if __name__ == "__main__":
    trainer = PotholeModelTrainer(epochs=100, batch_size=32)
    trainer.load_model()
    # trainer.train('./datasets/data.yaml')
    # trainer.evaluate('./datasets/data.yaml')
    # trainer.export_model('onnx')
