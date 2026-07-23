# Testing Guide

## Unit Tests

### Backend Tests

```bash
cd backend
pytest tests/ -v
```

### Test Coverage

```bash
pytest tests/ --cov=backend --cov-report=html
```

### Run Specific Test

```bash
pytest tests/test_detection.py -v
```

## Integration Tests

```bash
pytest tests/test_api.py -v
```

## Load Testing

Using Apache Bench:

```bash
ab -n 1000 -c 10 http://localhost:5000/health
```

Using locust:

```bash
locust -f tests/locustfile.py
```

## Frontend Tests

```bash
cd frontend
npm test
```

## Manual Testing

### Test Detection API

```bash
curl -X POST -F "image=@test.jpg" http://localhost:5000/api/detect/image
```

### Test Report Creation

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"latitude": 28.7041, "longitude": 77.1025, "severity": "severe"}' \
  http://localhost:5000/api/reports
```

## Performance Testing

### Image Processing Speed

```bash
python tests/test_performance.py
```

### Database Query Performance

```bash
EXPLAIN ANALYZE SELECT * FROM pothole_reports 
  WHERE ST_DWithin(location_point, ST_Point(28.7041, 77.1025)::geography, 1000);
```

## CI/CD Testing

GitHub Actions runs tests on every commit:

```yaml
- Unit tests
- Integration tests
- Code coverage
- Security scanning
- Linting
```

## Test Data

Sample test images and data available in `tests/fixtures/`

## Debugging

### Enable Debug Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Interactive Debugging

```python
import pdb; pdb.set_trace()
```
