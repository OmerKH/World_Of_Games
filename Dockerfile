# Use an appropriate base image
FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy application files
COPY main_score.py .
COPY utils.py .
COPY Scores.txt .
COPY requirements.txt .
COPY test/e2e.py .

# Ensure selenium is included in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Set the command to run the Flask application
CMD ["python", "main_score.py"]
