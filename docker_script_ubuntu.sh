#!/bin/bash

# Check if Docker is installed
if ! command -v docker &>/dev/null; then
    echo "Docker is not installed. Installing Docker..."
    sudo apt-get update
    sudo apt-get install -y docker.io
fi

# Check if git is installed
if ! command -v git &>/dev/null; then
    echo "Git is not installed. Installing Git..."
    sudo apt-get update
    sudo apt-get install -y git
fi

# Set custom configuration (modify as needed)
GITHUB_REPO="https://github.com/gil906/Twitter_Bot"
DOCKER_IMAGE_NAME="twitter_bot_image"
DOCKER_CONTAINER_NAME="twitter_bot_container"

# Pull the code from the GitHub repository
if [ ! -d "Twitter_Bot" ]; then
    git clone "$GITHUB_REPO"
fi

# Go to the project directory
cd Twitter_Bot

# Build Docker image with the code
sudo docker build -t "$DOCKER_IMAGE_NAME" .

# Run the Docker container (replace the environment variable placeholders)
sudo docker run -d \
    --name "$DOCKER_CONTAINER_NAME" \
    -e CONSUMER_KEY="YOUR_CONSUMER_KEY" \
    -e CONSUMER_SECRET="YOUR_CONSUMER_SECRET" \
    -e ACCESS_TOKEN="YOUR_ACCESS_TOKEN" \
    -e ACCESS_TOKEN_SECRET="YOUR_ACCESS_TOKEN_SECRET" \
    "$DOCKER_IMAGE_NAME"

# Optional: You can add other configuration options, such as port mapping or volume mounts, when running the container.

# Clean up: Remove the cloned repository (optional, if you don't need the code on the server)
cd ..
rm -rf Twitter_Bot
