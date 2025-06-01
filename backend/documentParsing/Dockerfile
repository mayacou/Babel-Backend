# Use a lightweight Python base image
FROM python:3.10-slim

# Set environment variable to suppress interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies (for OCR + PDF support)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    ghostscript \
    fonts-dejavu-core \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the default command to run the app
CMD ["python", "main.py"]
