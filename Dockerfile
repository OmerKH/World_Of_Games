# Build stages for a Python Flask application
FROM python:3.13-alpine AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    rm -rf /var/cache/apk/*

# Final stage
FROM python:3.13-alpine 
WORKDIR /app
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
# Copy app files
COPY main_score.py utils.py Scores.txt test/e2e.py ./
# Set environment variables for Flask
ENV FLASK_APP=app.py

EXPOSE 8777

CMD ["python3", "main_score.py"] 

