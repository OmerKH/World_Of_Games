FROM selenium/standalone-chrome:latest

# Install Python and pip
USER root
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

WORKDIR /app

# Create and activate virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

COPY main_score.py .
COPY utils.py .
COPY Scores.txt .
COPY requirements.txt .
COPY test/e2e.py .

# Install Python dependencies in virtual environment
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app.py

EXPOSE 8777

# Set correct permissions for application files
RUN chown -R seluser:seluser /app

# Switch back to non-root user for security
USER seluser

# Command to run both the application and tests
CMD python3 main_score.py 

# & sleep 5 && python3 e2e.py || exit 1 && wait