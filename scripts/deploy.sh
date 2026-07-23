#!/bin/bash
# Deployment script

echo "Starting deployment..."

# Build Docker images
echo "Building Docker images..."
docker-compose -f docker/docker-compose.yml build

# Start services
echo "Starting services..."
docker-compose -f docker/docker-compose.yml up -d

# Wait for services to be ready
echo "Waiting for services to be ready..."
sleep 10

# Check health
echo "Checking service health..."
curl http://localhost:5000/health

echo "Deployment completed!"
echo "Services running:"
docker-compose -f docker/docker-compose.yml ps
