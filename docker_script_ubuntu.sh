#!/bin/bash

# Function to check if Docker container is running
is_container_running() {
    local container_name="$1"
    local status=$(docker inspect -f "{{.State.Running}}" "$container_name" 2>/dev/null)
    [[ "$status" == "true" ]]
}

# Check if Docker is installed
if ! command -v docker &>/dev/null; then
    echo "Docker is not installed. Please install Docker and try again."
    exit 1
fi

# Check if git is installed
if ! command -v git &>/dev/null; then
    echo "Git is not installed. Please install Git and try again."
    exit 1
fi

# Set custom configuration (modify as needed)
GITHUB_REPO="https://github.com/gil906/Twitter_Bot"
DOCKER_IMAGE_NAME="twitter_bot_image"
DOCKER_CONTAINER_NAME="twitter_bot_container"

# Check if the Docker container is already running
if is_container_running "$DOCKER_CONTAINER_NAME"; then
    echo "The Docker container '$DOCKER_CONTAINER_NAME' is already running. Exiting..."
    exit 1
fi

# Pull the code from the GitHub repository
if [ ! -d "Twitter_Bot" ]; then
    git clone "$GITHUB_REPO"
fi

# Go to the project directory
cd Twitter_Bot

# Build Docker image with the code
if ! sudo docker build -t "$DOCKER_IMAGE_NAME" .; then
    echo "Failed to build the Docker image. Exiting..."
    cd ..
    rm -rf Twitter_Bot
    exit 1
fi

# Run the Docker container (replace the environment variable placeholders)
if ! sudo docker run -d \
    --name "$DOCKER_CONTAINER_NAME" \
    -e CONSUMER_KEY="YOUR_CONSUMER_KEY" \
    -e CONSUMER_SECRET="YOUR_CONSUMER_SECRET" \
    -e ACCESS_TOKEN="YOUR_ACCESS_TOKEN" \
    -e ACCESS_TOKEN_SECRET="YOUR_ACCESS_TOKEN_SECRET" \
    "$DOCKER_IMAGE_NAME"; then
    echo "Failed to run the Docker container. Exiting..."
    cd ..
    rm -rf Twitter_Bot
    exit 1
fi

# Optional: You can add other configuration options, such as port mapping or volume mounts, when running the container.

# Clean up: Remove the cloned repository (optional, if you don't need the code on the server)
cd ..
rm -rf Twitter_Bot

echo "Twitter bot is up and running in Docker container '$DOCKER_CONTAINER_NAME'."
