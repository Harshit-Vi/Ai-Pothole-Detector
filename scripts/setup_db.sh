#!/bin/bash
# Setup database script

echo "Setting up PostgreSQL database..."

# Create database
sudo -u postgres psql -c "CREATE DATABASE pothole_detector;"

# Create user
sudo -u postgres psql -c "CREATE USER pothole_user WITH PASSWORD 'secure_password';"

# Grant privileges
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE pothole_detector TO pothole_user;"

# Enable PostGIS
sudo -u postgres psql -d pothole_detector -c "CREATE EXTENSION PostGIS;"

echo "Database setup completed!"
