# API Documentation

## Detection Endpoints

### Detect Pothole from Image

**POST** `/api/detect/image`

Detect potholes in a single uploaded image.

**Request:**
```bash
curl -X POST -F "image=@pothole.jpg" http://localhost:5000/api/detect/image
```

**Response:**
```json
{
  "detections": [
    {
      "bbox": {
        "x1": 100,
        "y1": 150,
        "x2": 300,
        "y2": 350,
        "width": 200,
        "height": 200
      },
      "confidence": 0.92,
      "severity": "severe",
      "severity_score": 0.85
    }
  ],
  "image_shape": [640, 480, 3],
  "success": true
}
```

### Detect from URL

**POST** `/api/detect/url`

**Request:**
```json
{
  "image_url": "https://example.com/image.jpg"
}
```

### Batch Detection

**POST** `/api/detect/batch`

Detect in multiple images at once.

---

## Report Endpoints

### Get All Reports

**GET** `/api/reports`

**Query Parameters:**
- `severity`: Filter by severity (minor, medium, severe)
- `status`: Filter by status (reported, acknowledged, resolved)
- `limit`: Number of results (default: 100)
- `offset`: Pagination offset (default: 0)

**Response:**
```json
{
  "reports": [
    {
      "id": 1,
      "latitude": 28.7041,
      "longitude": 77.1025,
      "address": "Main Street, Delhi",
      "severity": "severe",
      "severity_score": 0.85,
      "status": "reported",
      "reported_at": "2024-07-23T10:30:00"
    }
  ],
  "total": 42
}
```

### Get Single Report

**GET** `/api/reports/{report_id}`

### Create Report

**POST** `/api/reports`

**Request:**
```json
{
  "latitude": 28.7041,
  "longitude": 77.1025,
  "severity": "severe",
  "description": "Large pothole on main road"
}
```

---

## Dashboard Endpoints

### Get Statistics

**GET** `/api/dashboard/stats`

**Response:**
```json
{
  "total_reports": 150,
  "total_detections": 300,
  "by_severity": {
    "minor": 100,
    "medium": 150,
    "severe": 50
  }
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "error": "No image provided"
}
```

### 404 Not Found
```json
{
  "error": "Report not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error"
}
```

---

## Rate Limiting

API endpoints have rate limiting to prevent abuse:
- 100 requests per minute for detection endpoints
- 500 requests per minute for reporting endpoints

---

## Authentication

Current version supports basic authentication. Future versions will include:
- JWT tokens
- OAuth2 integration
- API key management
