FROM python:3.9

# Working directory
WORKDIR /app

# Copy application files
COPY main_score.py ./
COPY utils.py ./
COPY Scores.txt ./
COPY requirements.txt ./
COPY test/e2e.py ./

# Install Google Chrome
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y google-chrome-stable \
    && apt-get clean

# Install Python dependencies

# Create a virtual environment and install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt



# Expose the port the app runs on
EXPOSE 5000

# Set the command to run the Flask application
CMD ["python3", "main_score.py"]


#docker exec -it wog_flask python3 /app/e2e.py
