# Use an official Python image as a base image
FROM python:3.8-alpine

# Set the working directory
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Specify the command to run when the container starts
CMD ["python", "run.py"]
