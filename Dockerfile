# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for API credentials
ENV TWITTER_CONSUMER_KEY="YOUR_CONSUMER_KEY"
ENV TWITTER_CONSUMER_SECRET="YOUR_CONSUMER_SECRET"
ENV TWITTER_ACCESS_TOKEN="YOUR_ACCESS_TOKEN"
ENV TWITTER_ACCESS_TOKEN_SECRET="YOUR_ACCESS_TOKEN_SECRET"

# Set environment variable for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Create and set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary packages
RUN pip install tweepy

# Run your Python script
CMD ["python", "your_twitter_bot_script.py"]
