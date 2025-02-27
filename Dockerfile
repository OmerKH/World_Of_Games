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


# # Install necessary packages for Chrome
# RUN apt-get update && apt-get install -y \
#     wget \
#     gnupg2 \
#     && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
#     && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list \
#     && apt-get update && apt-get install -y google-chrome-stable \
#     && apt-get clean

# Expose the port the app runs on
EXPOSE 5000

# Set the command to run the Flask application

# Set the command to run the Flask application
CMD ["python", "main_score.py"]



#Build - docker build -t flaskapp .

#Run - docker run -p 5000:5000 wog_flask
