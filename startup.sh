#!/bin/bash

# This script runs when deploying to Azure App Service

# Install dependencies
pip install -r requirements.txt

# Create database directory if needed
mkdir -p /tmp

# Run migrations if needed
python -c "from database import engine, Base; Base.metadata.create_all(bind=engine)"

# Start the application with gunicorn
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
