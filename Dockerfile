# Use the existing image as the base
FROM ghcr.io/bart-jansen/aoai-simulated-api:latest

# Copy forwarders and openai deployment config into the image
WORKDIR /app
COPY . .