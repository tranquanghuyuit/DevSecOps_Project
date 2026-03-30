# Stage 1: Build stage
# Use a specific, lightweight base image
FROM python:3.9-slim as builder


# Set the working directory
WORKDIR /app
RUN pip install --no-cache-dir --upgrade pip setuptools wheel
# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY . .

# Stage 2: Final stage
# Use a minimal, non-root base image for security
FROM python:3.9-slim
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Copy installed packages and source code from the builder stage
COPY --from=builder /app /home/appuser
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.main:app"]

# Command to run the application
CMD ["python", "src/main.py"]





