# Use official Python image as base
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# RUN apt-get update && apt-get install -y netcat-openbsd

# RUN mkdir -p /app/staticfiles

# Expose port 8000 (Django default)
EXPOSE 8000

# Copy entrypoint script and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use entrypoint script to handle migrations
ENTRYPOINT ["/entrypoint.sh"]
