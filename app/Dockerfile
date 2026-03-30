# Stage 1: Build stage - Create a wheelhouse
FROM python:3.9-slim as builder

WORKDIR /app

# First, upgrade pip and setuptools in the builder to ensure they are clean
RUN pip install --no-cache-dir --upgrade pip setuptools

# Now, create the wheelhouse using the clean setuptools
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir=/app/wheels -r requirements.txt

# Stage 2: Final stage
FROM python:3.9-slim
RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# Create a non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Copy application code
COPY . /home/appuser

# Copy wheels from builder and install, then clean up
COPY --from=builder /app/wheels /wheels
RUN pip install --no-cache-dir /wheels/* && rm -rf /wheels

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.main:app"]





