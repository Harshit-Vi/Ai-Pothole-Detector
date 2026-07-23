# AI Pothole Detector 🚗🛣️

## Real-Time Pothole & Road Damage Detection & Auto-Reporting System

An AI-powered system that detects potholes and road damage from live video/images, automatically tags GPS location, and files reports to municipal authorities in real-time.

![Project Status](https://img.shields.io/badge/status-in--development-yellow)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![React](https://img.shields.io/badge/react-18%2B-61dafb)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🎯 Objective

Build a comprehensive system that:
1. **Detects potholes** in real-time using YOLOv8 object detection
2. **Classifies severity** (Minor/Medium/Severe)
3. **Tags GPS location** automatically
4. **Sends notifications** to municipal authorities via SMS/Email
5. **Visualizes data** on interactive map dashboard
6. **Enables citizen reporting** via mobile app

---

## 🎨 Key Features

### 🔍 Detection & Analysis
- Real-time pothole detection from dashcam/phone camera
- Automatic GPS location tagging with PostGIS geospatial queries
- Severity classification (Minor/Medium/Severe)
- Image processing and validation pipeline

### 🚨 Notifications
- Auto-SMS reports to municipality via Twilio
- Auto-Email reports via SendGrid
- Async task processing with Celery + Redis
- Municipality contact management

### 📊 Dashboard & Analytics
- Interactive web dashboard with Leaflet.js map
- Live pothole visualization
- Statistics and filtering capabilities
- Admin panel for municipality management
- Historical road condition tracking

### 📱 Mobile App
- React Native cross-platform app (iOS + Android)
- Live camera feed integration
- GPS location capture
- Quick report submission
- Map view of reported potholes

### 🏗️ Infrastructure
- Containerized deployment with Docker
- CI/CD pipeline with GitHub Actions
- Scalable cloud hosting (AWS/GCP ready)
- Monitoring with Prometheus + Grafana

---

## 👥 Target Users

- **Municipal Corporations** - Track road condition data
- **Delivery Drivers** (Flipkart, Zomato, Amazon) - Report during delivery routes
- **Citizens** - Report potholes from dashcams or phones

---

## 📦 Tech Stack

### Backend
| Component | Technology | Why |
|-----------|-----------|-----|
| Framework | Flask/FastAPI | Lightweight, perfect for ML APIs |
| Detection | YOLOv8 (Ultralytics) | Fastest real-time detection |
| Python | 3.9+ | Full ML library support |
| Database | PostgreSQL + PostGIS | Geospatial queries |
| ORM | SQLAlchemy | Clean database modeling |
| Async | Celery + Redis | Handle notifications without blocking |
| Notifications | Twilio + SendGrid | SMS/Email alerts |
| Maps | Folium/Leaflet.js | Interactive visualization |

### Frontend (Web Dashboard)
| Component | Technology | Why |
|-----------|-----------|-----|
| Framework | React.js | Interactive UI |
| Maps | Leaflet.js | Interactive map component |
| Charts | Chart.js/Recharts | Statistics visualization |
| HTTP Client | Axios | API requests |
| State Management | Redux/Context API | State handling |
| UI Framework | Material-UI/Tailwind | Pre-built components |

### Mobile App
| Component | Technology | Why |
|-----------|-----------|-----|
| Framework | React Native | Cross-platform (iOS + Android) |
| Camera | react-native-camera | Live camera feed |
| GPS | react-native-geolocation | Location tagging |
| Maps | react-native-maps | Mobile map display |

### ML/Training
| Component | Technology | Why |
|-----------|-----------|-----|
| Model | YOLOv8n (Nano) | Lightweight, fast |
| Framework | PyTorch (Ultralytics) | Production-ready |
| Dataset | RDD2020 | 9,000+ pothole images |
| Training | Google Colab/AWS SageMaker | Free GPU |
| Optimization | ONNX/TensorRT | Edge deployment |

### Infrastructure
| Component | Technology | Why |
|-----------|-----------|-----|
| Cloud | AWS EC2/Google Cloud | Scalability |
| GPU | NVIDIA T4/L4 | Fast inference |
| Storage | S3/Google Cloud Storage | Image storage |
| Database Hosting | AWS RDS | Managed PostgreSQL |
| Monitoring | Prometheus + Grafana | System health |
| CI/CD | GitHub Actions | Automated testing & deployment |

---

## 📁 Directory Structure

```
Ai-Pothole-Detector/
│
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── .env.example
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── database/
│   └── utils/
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── .env.example
│
├── mobile/
│   ├── src/
│   ├── app.json
│   ├── package.json
│   └── .env.example
│
├── training/
│   ├���─ train_model.py
│   ├── dataset_download.py
│   ├── datasets/
│   └── notebooks/
│
├── docs/
│   ├── API.md
│   ├── SETUP.md
│   ├── ARCHITECTURE.md
│   └── TESTING.md
│
├── tests/
├── scripts/
└── docker/
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 16+
- PostgreSQL 12+
- Docker & Docker Compose

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm start
```

### Mobile App Setup
```bash
cd mobile
npm install
npm start
```

### Training Pipeline
```bash
cd training
pip install -r requirements.txt
python train_model.py
```

---

## 📋 Implementation Timeline

| Phase | Duration | Tasks |
|-------|----------|-------|
| Phase 1: Setup & Model | Week 1-2 | Clone repo, install YOLOv8, download dataset, train model |
| Phase 2: Backend API | Week 2-3 | Flask setup, YOLOv8 integration, PostgreSQL, GPS, severity |
| Phase 3: Notifications | Week 3-4 | Twilio, SendGrid, Celery, async jobs |
| Phase 4: Frontend | Week 4-5 | React dashboard, Leaflet maps, filters, statistics |
| Phase 5: Mobile | Week 5-6 | React Native, camera, GPS, report form |
| Phase 6: Deployment | Week 6-7 | Docker, AWS/GCP, CI/CD, testing |

---

## 📚 Documentation

- [API Documentation](./docs/API.md) - Complete API endpoints
- [Setup Guide](./docs/SETUP.md) - Detailed installation
- [Architecture Guide](./docs/ARCHITECTURE.md) - System design & flow
- [Testing Guide](./docs/TESTING.md) - Unit & integration tests

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](./LICENSE) file for details.

---

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Check existing documentation
- Review API documentation

---

## 🎯 Roadmap

- [ ] Phase 1: YOLOv8 model training
- [ ] Phase 2: Backend API development
- [ ] Phase 3: Notification system
- [ ] Phase 4: Web dashboard
- [ ] Phase 5: Mobile app
- [ ] Phase 6: Production deployment
- [ ] Real-time WebSocket updates
- [ ] Advanced analytics & ML features
- [ ] Integration with municipal systems
- [ ] Mobile app (iOS & Android stores)

---

**Built with ❤️ for safer roads** 🛣️✨
