# Setup Guide

## System Requirements

- Python 3.9+
- Node.js 16+
- PostgreSQL 12+
- Docker & Docker Compose (optional)
- GPU with CUDA support (recommended for training)

## Backend Setup

### 1. Install Python Dependencies

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Setup Database

```bash
# Create PostgreSQL database
psql -U postgres
CREATE DATABASE pothole_detector;
CREATE USER pothole_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE pothole_detector TO pothole_user;
\c pothole_detector
CREATE EXTENSION PostGIS;
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with your settings
```

### 4. Initialize Database

```bash
python backend/database/db_init.py
```

### 5. Download Models

```bash
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

### 6. Run Backend

```bash
python backend/app.py
```

Backend will be available at `http://localhost:5000`

## Frontend Setup

### 1. Install Node Dependencies

```bash
cd frontend
npm install
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env with your API URL
```

### 3. Start Development Server

```bash
npm start
```

Frontend will be available at `http://localhost:3000`

## Mobile App Setup

### 1. Install Dependencies

```bash
cd mobile
npm install
```

### 2. Android Setup

```bash
npm run android
```

### 3. iOS Setup

```bash
npm run ios
```

## Docker Deployment

### 1. Build and Run

```bash
cd docker
docker-compose up -d
```

### 2. Verify Services

```bash
# Check backend
curl http://localhost:5000/health

# Check database
psql -h localhost -U pothole_user -d pothole_detector

# Check Redis
redis-cli ping
```

## Training Setup

### 1. Install Training Dependencies

```bash
cd training
pip install -r requirements.txt
```

### 2. Download Dataset

```bash
python dataset_download.py
```

### 3. Start Training

```bash
python train_model.py
```

## Verification

### Test Backend API

```bash
# Health check
curl http://localhost:5000/health

# Test detection endpoint
curl -X POST -F "image=@test.jpg" http://localhost:5000/api/detect/image
```

### Test Frontend

Open browser to `http://localhost:3000`

## Troubleshooting

### Database Connection Error

```bash
# Check PostgreSQL is running
sudo systemctl status postgresql

# Check connection string in .env
DATABASE_URL=postgresql://user:password@localhost:5432/pothole_detector
```

### Model Download Failed

```bash
# Manual model download
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt').info()"
```

### Port Already in Use

```bash
# Change port in .env or run on different port
FLASK_PORT=5001 python backend/app.py
```
