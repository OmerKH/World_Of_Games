# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install Flask (and any other dependencies)
RUN pip install Flask

# Copy the Flask application and the Scores.txt file into the container
COPY main_score.py .
COPY utils.py .
COPY Scores.txt .

# Expose the port the app runs on
EXPOSE 5000

# Set the command to run the Flask application
CMD ["python", "main_score.py"]