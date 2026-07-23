# System Architecture

## Overview

The AI Pothole Detector is a distributed system with the following components:

```
┌─────────────────────────────────────────┐
│ Frontend (React) / Mobile (React Native)│
│ Dashboard + Map + Analytics             │
└──────────────────┬──────────────────────┘
                   │
          HTTP/REST API
                   │
┌──────────────────▼──────────────────────┐
│ Flask/FastAPI Backend                   │
├──────────────────────────────────────────┤
│ ┌────────────────────────────────────┐  │
│ │ YOLOv8 Detection Model             │  │
│ │ (Pothole + Severity)               │  │
│ └────────────────────────────────────┘  │
│ ┌────────────────────────────────────┐  │
│ │ GPS + Location Tagging             │  │
│ └────────────────────────────────────┘  │
│ ┌────────────────────────────────────┐  │
│ │ Celery (Async Tasks)               │  │
│ │ - Send SMS/Email                   │  │
│ │ - Generate Reports                 │  │
│ └────────────────────────────────────┘  │
└──────────────────┬──────────────────────┘
      │        │        │
      │        │        │
  ┌───▼──┐ ┌──▼──┐ ┌───▼────┐
  │  DB  │ │Redis│ │ S3     │
  │ Pg   │ │Cache│ │Storage │
  │ GIS  │ │     │ │        │
  └──────┘ └─────┘ └────────┘
```

## Components

### Frontend Layer

- **React Dashboard**: Web-based UI for monitoring potholes
- **Leaflet Maps**: Interactive map visualization
- **Charts/Statistics**: Analytics dashboard
- **Responsive Design**: Mobile-friendly interface

### Backend Layer

- **Flask/FastAPI**: REST API server
- **YOLOv8 Detection**: Real-time pothole detection
- **GPS Service**: Location tagging and geocoding
- **Notification Service**: SMS/Email alerts via Twilio/SendGrid
- **Database Service**: CRUD operations

### Data Layer

- **PostgreSQL**: Primary database with PostGIS
- **Redis**: Caching and task queue
- **S3/Cloud Storage**: Image storage

### Async Processing

- **Celery**: Distributed task queue
- **Redis**: Message broker
- **Background Jobs**: Notifications, report generation

## Data Flow

### Detection Pipeline

1. User uploads image via mobile app or dashboard
2. Image sent to backend API
3. YOLOv8 model processes image
4. Detections returned with severity classification
5. GPS coordinates tagged automatically
6. Results saved to database
7. Async task queued for notifications
8. SMS/Email sent to municipality
9. Map updated in real-time

### Reporting Pipeline

1. Detection results stored in database
2. Severity and location analyzed
3. Report generated with metadata
4. Municipality contacts fetched
5. Notifications sent asynchronously
6. Report status tracked
7. Dashboard updated

## Technology Decisions

### Why YOLOv8?

- Real-time detection capability
- High accuracy (85%+ mAP)
- Lightweight for edge devices
- Pre-trained weights available
- Active community support

### Why Flask?

- Lightweight and flexible
- Excellent for ML APIs
- Easy to deploy and scale
- Good integration with ML libraries

### Why PostgreSQL + PostGIS?

- Geospatial queries (radius search)
- Open-source and reliable
- JSONB support for flexible schemas
- Strong community

### Why Celery + Redis?

- Async task processing
- Non-blocking notifications
- Scalable job queue
- Reliable delivery

## Deployment Architecture

### Docker Setup

```
┌──────────────────────────────────────┐
│ Docker Compose                       │
├──────────────────────────────────────┤
│ ┌──────────┐ ┌──────────┐ ┌────────┐│
│ │ Nginx    │ │ Backend  │ │ Celery ││
│ │ (Proxy)  │ │ (Flask)  │ │(Worker)││
│ └──────────┘ └──────────┘ └────────┘│
│        ↓              ↓              │
│ ┌──────────────┐  ┌──────────────┐  │
│ │ PostgreSQL   │  │ Redis        │  │
│ └──────────────┘  └──────────────┘  │
└──────────────────────────────────────┘
```

### Cloud Deployment

- **Compute**: AWS EC2 / Google Cloud Run
- **Database**: AWS RDS PostgreSQL
- **Cache**: ElastiCache Redis
- **Storage**: S3 / Google Cloud Storage
- **CI/CD**: GitHub Actions
- **Monitoring**: CloudWatch / Stackdriver

## Performance Considerations

### Detection Speed

- Target: < 100ms inference per image
- YOLOv8 Nano: ~50ms on GPU
- Batch processing: 10-20 images/sec

### Scalability

- Horizontal scaling via API replicas
- Redis pub/sub for real-time updates
- Database connection pooling
- CDN for static assets

### Database Optimization

- Indexes on frequently queried columns
- Partitioning by time for large tables
- Read replicas for analytics queries

## Security

- HTTPS/TLS encryption
- Input validation and sanitization
- Rate limiting on API endpoints
- Database encryption at rest
- Secrets management (environment variables)
- Authentication for sensitive endpoints

## Monitoring

- Application logs: ELK Stack or CloudWatch
- Metrics: Prometheus + Grafana
- APM: New Relic or DataDog
- Alerts: PagerDuty integration
