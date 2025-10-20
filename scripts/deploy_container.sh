#!/bin/bash

# Step 1: Define image name
IMAGE_NAME="Finance-Agent"

# Step 2: Remove existing container if running
docker rm -f finance_agent_container 2>/dev/null

# Step 3: Build Docker image
echo "🚧 Building Docker image: $IMAGE_NAME"
docker build -t $IMAGE_NAME .

# Step 4: Run container
echo "🚀 Running container on port 8501"
docker run -d -p 8501:8501 --name finance_agent_container $IMAGE_NAME

# Step 5: Confirm status
echo "✅ Container 'finance_agent_container' is running. Access the app at http://localhost:8501"
in 