FROM python:3.9-alpine3.21

# Working directory
WORKDIR /app

# Copy application files
COPY main_score.py ./
COPY utils.py ./
COPY Scores.txt ./
COPY requirements.txt ./
COPY test/e2e.py ./

# Install Google Chrome
RUN apk add --no-cache \
    chromium \
    && apk add --no-cache \
    chromium-chromedriver \
    && rm -rf /var/cache/apk/*

# Create a virtual environment and install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

#docker exec -it wog_flask python3 /app/e2e.py
CMD ["sh", "-c", "python3 main_score.py && sleep 10 && python3 e2e.py"]


# Set the command to run the Flask application
# CMD ["python3", "main_score.py"]