FROM python:3.9-alpine3.21

# Working directory
WORKDIR /app


# Copy application files
COPY main_score.py .
COPY utils.py .
COPY Scores.txt .
COPY requirements.txt .
COPY test/e2e.py .

# Ensure selenium is included in requirements.txt
RUN apk add --no-cache \
    chromium \
    && apk add --no-cache \
    chromium-chromedriver \
    && rm -rf /var/cache/apk/*




RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on

# Set the command to run the Flask application and then the e2e tests
CMD ["sh", "-c", "python3 main_score.py & sleep 10 && python3 e2e.py"]
