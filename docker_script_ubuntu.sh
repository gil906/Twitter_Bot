#!/bin/bash

# Step 1: Install Docker (if not already installed)
sudo apt-get update
sudo apt-get install -y docker.io

# Step 2: Pull the code from the GitHub repository
git clone https://github.com/gil906/Twitter_Bot
cd Twitter_Bot

# Step 3: Build Docker image with the code
sudo docker build -t twitter_bot_image .

# Step 4: Run the Docker container
sudo docker run -d --name twitter_bot_container twitter_bot_image

# Optional: You can add other configuration options, such as port mapping or environment variables, when running the container.

# Clean up: Remove the cloned repository (optional, if you don't need the code on the server)
cd ..
rm -rf Twitter_Bot
