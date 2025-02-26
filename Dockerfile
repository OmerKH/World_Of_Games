FROM python:3.9-slim

# Working directory
WORKDIR /app

# RUN pip install Flask

# Copy application files
COPY main_score.py .
COPY utils.py .
COPY Scores.txt .
COPY test/e2e.py ./src/
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt




# Expose the port the app runs on
EXPOSE 5000

# Set the command to run the Flask application
CMD ["python", "main_score.py"]



#Build - docker build -t flaskapp .

#Run - docker run -p 5000:5000 wog_flask

####################################################################
# using utils?
####################################################################


# Copy requirements first to leverage Docker cache
# 

# Install all dependencies
# RUN pip install --no-cache-dir -r requirements.txt
