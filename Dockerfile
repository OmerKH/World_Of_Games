FROM python:3.9-alpine3.21

# Install Google Chrome
RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    && ln -s /usr/bin/chromium-browser /usr/bin/google-chrome \
    && ln -s /usr/bin/chromedriver /usr/local/bin/chromedriver



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


# Expose the port the app runs on and set the display port for Chrome

EXPOSE 5000

# Set the command to run the Flask application
CMD ["python3", "main_score.py"]
