# Stage 1: Build stage - Create a clean venv
FROM python:3.9-slim as builder

# Create a virtual environment
RUN python -m venv /opt/venv

# Activate the virtual environment and upgrade pip
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir --upgrade pip

# Copy requirements and install into the venv
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Final stage
FROM python:3.9-slim
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Copy the virtual environment from the builder stage
COPY --from=builder /opt/venv /home/appuser/venv

# Copy the application source code
COPY . /home/appuser

# Activate the venv for the final command
ENV PATH="/home/appuser/venv/bin:$PATH"

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application using Gunicorn from the venv
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.main:app"]





