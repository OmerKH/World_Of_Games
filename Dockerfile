FROM selenium/standalone-chrome:latest



# Working directory
WORKDIR /app

# Copy application files
COPY main_score.py .
COPY utils.py .
COPY Scores.txt .
COPY requirements.txt .
COPY test/e2e.py .

# Ensure selenium is included in requirements.txt and other dependencies
USER root # Ensure root privileges

USER root
RUN apt-get update && \
    apt-get install -y python3-venv && \
    python3 -m venv venv && \
    venv/bin/pip install --no-cache-dir -r requirements.txt






# Expose the port the app runs on
EXPOSE 5000

# Set the command to run the Flask application

# Set the command to run the Flask application
CMD ["venv/bin/python", "main_score.py"]




#Build - docker build -t flaskapp .

#Run - docker run -p 5000:5000 wog_flask

####################################################################
# using utils?
####################################################################


# Copy requirements first to leverage Docker cache
# 

# Install all dependencies
# RUN pip install --no-cache-dir -r requirements.txt
