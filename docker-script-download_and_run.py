# This script  downloads the files from this repo (https://github.com/gil906/Twitter_Bot) and runs the Twitter bot inside a Docker container:

import os
import shutil
import subprocess
import requests
from zipfile import ZipFile

# GitHub repository URL
repo_url = "https://github.com/gil906/Twitter_Bot/archive/main.zip"
repo_zip_file = "Twitter_Bot-main.zip"

# Function to download the GitHub repository as a zip file
def download_repo_zip(url, destination_file):
    response = requests.get(url)
    with open(destination_file, 'wb') as f:
        f.write(response.content)

# Function to extract the zip file
def extract_zip_file(zip_file, destination_folder):
    with ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

# Function to run the Docker container
def run_docker_container():
    subprocess.run(["docker", "build", "-t", "twitter-bot", "."])
    subprocess.run(["docker", "run", "-d", "--name", "twitter-bot-container", "twitter-bot"])

def main():
    # Download the GitHub repository as a zip file
    print("Downloading the GitHub repository...")
    download_repo_zip(repo_url, repo_zip_file)
    print("GitHub repository downloaded successfully.")

    # Create a folder to extract the contents of the zip file
    extract_folder = "twitter_bot_files"
    os.makedirs(extract_folder, exist_ok=True)

    # Extract the contents of the zip file
    print("Extracting the downloaded zip file...")
    extract_zip_file(repo_zip_file, extract_folder)
    print("Extraction completed.")

    # Move the bot.py and Dockerfile to the current directory
    source_folder = os.path.join(extract_folder, "Twitter_Bot-main")
    shutil.move(os.path.join(source_folder, "bot.py"), "bot.py")
    shutil.move(os.path.join(source_folder, "Dockerfile"), "Dockerfile")

    # Clean up by removing the downloaded zip file and the extracted folder
    os.remove(repo_zip_file)
    shutil.rmtree(extract_folder)

    # Run the Docker container
    print("Building and running the Docker container...")
    run_docker_container()
    print("Twitter bot is now running in a Docker container.")

if __name__ == "__main__":
    main()
