#!/bin/bash

# This script runs when deploying to Azure App Service

cd /home/site/wwwroot

# Use Python 3.11 from Azure's runtime
/usr/local/bin/python3.11 -m pip install --no-cache-dir -r requirements.txt

# Create database directory if needed
mkdir -p /tmp

# Run the application
/usr/local/bin/python3.11 -m gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --timeout 600
