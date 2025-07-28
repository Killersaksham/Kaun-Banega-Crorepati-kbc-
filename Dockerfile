# Use official Python base image with system tools
FROM python:3.10-slim

# Install system dependencies for pygame
RUN apt-get update && \
    apt-get install -y libsdl2-dev libsmpeg-dev libasound2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev libjpeg-dev libfreetype6-dev && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy your code into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
