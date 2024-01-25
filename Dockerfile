# Use the official Alpine image with Python 3.8
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Install dependencies
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip && \
    pip3 install Flask prometheus-flask-exporter

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 5000
EXPOSE 5000

# Define the command to run your application
CMD ["python3", "run.py"]
