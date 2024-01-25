# Use the official Python 3.8 Alpine image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 5000
EXPOSE 5000

# Define the command to run your application
CMD ["python", "run.py"]
