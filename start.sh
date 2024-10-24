#!/bin/bash

# Stop and remove the existing container if it's running
docker stop vibe-api-container 2>/dev/null
docker rm vibe-api-container 2>/dev/null

# Build the Docker image
docker build -t vibe-api .

# Run the container
docker run  -p 8000:8000 --name vibe-api-container -v $(pwd):/app vibe-api
