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

# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && wget -q -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i /tmp/google-chrome.deb; apt-get -y install -f \
    && rm /tmp/google-chrome.deb \
    && wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && chmod +x /usr/local/bin/chromedriver \
    && rm /tmp/chromedriver.zip

# Set the command to run the Flask application
CMD ["python", "main_score.py"]
