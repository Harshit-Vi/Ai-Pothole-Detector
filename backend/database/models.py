"""SQLAlchemy models for database."""
from datetime import datetime
from backend.database.db_init import db
from geoalchemy2 import Geometry

class PotholeReport(db.Model):
    """Pothole report model."""
    __tablename__ = 'pothole_reports'
    
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    location_point = db.Column(Geometry('POINT'), nullable=True)
    address = db.Column(db.String(500), nullable=True)
    severity = db.Column(db.String(20), default='minor')
    severity_score = db.Column(db.Float, default=0.0)
    detection_confidence = db.Column(db.Float, nullable=True)
    image_path = db.Column(db.String(500), nullable=True)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='reported')  # reported, acknowledged, resolved
    reported_by = db.Column(db.String(100), nullable=True)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        """Convert model to dictionary."""
        return {
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'address': self.address,
            'severity': self.severity,
            'severity_score': self.severity_score,
            'status': self.status,
            'reported_at': self.reported_at.isoformat() if self.reported_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Detection(db.Model):
    """Detection record model."""
    __tablename__ = 'detections'
    
    id = db.Column(db.Integer, primary_key=True)
    image_path = db.Column(db.String(500), nullable=False)
    bbox_x1 = db.Column(db.Float, nullable=False)
    bbox_y1 = db.Column(db.Float, nullable=False)
    bbox_x2 = db.Column(db.Float, nullable=False)
    bbox_y2 = db.Column(db.Float, nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    severity = db.Column(db.String(20), nullable=True)
    severity_score = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert model to dictionary."""
        return {
            'id': self.id,
            'image_path': self.image_path,
            'bbox': {'x1': self.bbox_x1, 'y1': self.bbox_y1, 'x2': self.bbox_x2, 'y2': self.bbox_y2},
            'confidence': self.confidence,
            'severity': self.severity,
            'severity_score': self.severity_score,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class Municipality(db.Model):
    """Municipality contact information model."""
    __tablename__ = 'municipalities'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    address = db.Column(db.Text, nullable=True)
    city = db.Column(db.String(100), nullable=True)
    state = db.Column(db.String(100), nullable=True)
    country = db.Column(db.String(100), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        """Convert model to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'city': self.city,
            'state': self.state
        }
