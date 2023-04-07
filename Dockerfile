# Use an official Python runtime as a parent image
FROM python:3.9-slim

USER root

# Set the working directory to /app
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y ffmpeg && \
    apt-get install -y wget git gcc libasound2-dev portaudio19-dev 

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pwd
RUN pip install Flask

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP server.py
ENV FLASK_RUN_HOST 0.0.0.0

# Run app.py when the container launches
CMD ["flask", "run"]
