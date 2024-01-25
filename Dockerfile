# Use an official Docker image as a base image
FROM alpine:latest

# Set the working directory
WORKDIR /app

# Copy the contents of the current directory into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir Flask


# Expose port 5000
EXPOSE 5000

# Define the command to run your application
CMD ["python", "run.py"]
