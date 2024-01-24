# Use an official Docker image as a base image
FROM alpine:latest

# Set the working directory
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Specify the command to run when the container starts
CMD ["echo", "Hello, Docker!"]
