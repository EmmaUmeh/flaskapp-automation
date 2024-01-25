# Use an official Python image as a base image
FROM python:3.8-alpine

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the contents of the current directory into the container at /app
COPY . /app

# Expose the port that your Flask app will run on
EXPOSE 5000

# Specify the command to run when the container starts
CMD ["python", "run.py"]
