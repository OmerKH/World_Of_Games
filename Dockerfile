FROM python:3.13-alpine

WORKDIR /app

# Copy app files
COPY main_score.py .
COPY utils.py .
COPY Scores.txt .
COPY requirements.txt .
COPY test/e2e.py .

# Install Python dependencies 
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app.py

EXPOSE 8777

CMD python3 main_score.py 

# & sleep 5 && python3 e2e.py || exit 1 && wait