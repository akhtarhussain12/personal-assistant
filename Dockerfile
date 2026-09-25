# Use a lightweight Python base image
FROM python:3.14-slim

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Ollama port (optional)
EXPOSE 11434

# Environment variable for Ollama host (connects to host machine)
ENV OLLAMA_HOST=http://host.docker.internal:11434/v1

# Run your agent
CMD ["python", "agent.py"]
