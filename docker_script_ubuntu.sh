Certainly! Here's an optimized version of the script with improved error handling, better messaging, and reduced redundancy:

```bash
#!/bin/bash

# Function to check if Docker container is running
is_container_running() {
    local container_name="$1"
    docker inspect -f "{{.State.Running}}" "$container_name" 2>/dev/null | grep -q "true"
}

# Function to display an error message and exit
exit_with_error() {
    echo "Error: $1"
    exit 1
}

# Check if Docker is installed
if ! command -v docker &>/dev/null; then
    exit_with_error "Docker is not installed. Please install Docker and try again."
fi

# Check if git is installed
if ! command -v git &>/dev/null; then
    exit_with_error "Git is not installed. Please install Git and try again."
fi

# Set custom configuration (modify as needed)
GITHUB_REPO="https://github.com/gil906/Twitter_Bot"
DOCKER_IMAGE_NAME="twitter_bot_image"
DOCKER_CONTAINER_NAME="twitter_bot_container"

# Check if the Docker container is already running
if is_container_running "$DOCKER_CONTAINER_NAME"; then
    exit_with_error "The Docker container '$DOCKER_CONTAINER_NAME' is already running. Exiting..."
fi

# Pull the code from the GitHub repository
if [ ! -d "Twitter_Bot" ]; then
    git clone "$GITHUB_REPO" || exit_with_error "Failed to clone the GitHub repository. Exiting..."
fi

# Go to the project directory
cd Twitter_Bot

# Build Docker image with the code
if ! sudo docker build -t "$DOCKER_IMAGE_NAME" .; then
    exit_with_error "Failed to build the Docker image. Exiting..."
fi

# Run the Docker container (replace the environment variable placeholders)
if ! sudo docker run -d \
    --name "$DOCKER_CONTAINER_NAME" \
    -e CONSUMER_KEY="YOUR_CONSUMER_KEY" \
    -e CONSUMER_SECRET="YOUR_CONSUMER_SECRET" \
    -e ACCESS_TOKEN="YOUR_ACCESS_TOKEN" \
    -e ACCESS_TOKEN_SECRET="YOUR_ACCESS_TOKEN_SECRET" \
    "$DOCKER_IMAGE_NAME"; then
    exit_with_error "Failed to run the Docker container. Exiting..."
fi

# Clean up: Remove the cloned repository (optional, if you don't need the code on the server)
cd ..
rm -rf Twitter_Bot

echo "Twitter bot is up and running in Docker container '$DOCKER_CONTAINER_NAME'."
```

In this optimized version, the error handling is consolidated into a single function (`exit_with_error`) to reduce redundancy. The script provides more informative error messages and exits gracefully in case of any issues. The overall structure and logic remain the same, but the script is now more concise and efficient.

Remember to replace the placeholders with your actual Twitter API credentials before running the script. Enjoy your optimized Twitter bot running in a Docker container!
