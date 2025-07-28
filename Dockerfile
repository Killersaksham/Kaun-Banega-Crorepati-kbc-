# Use a lightweight Python base image
FROM python:3.10-slim

# Install required system packages for pygame and playsound
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libsdl2-dev \
    libsmpeg-dev \
    libasound2-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    libjpeg-dev \
    libfreetype6-dev \
    ffmpeg \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the app (change to your actual entry file)
CMD ["python", "kbc_web.py"]
