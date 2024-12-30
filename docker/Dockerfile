# Use Python as base image
FROM python:3.10-slim

LABEL maintainer="alan.sung"

LABEL email="meng.s.song@gmail.com"

# Set up work dir
WORKDIR /app

# Copy code
COPY ../src /app/src
COPY ../requirements.txt /app/

# Install required packages
RUN pip install -r requirements.txt

# Make lookup-cli as executable command
RUN chmod +x /app/src/lookup-cli && \
    ln -s /app/src/lookup-cli /usr/local/bin/lookup-cli

# Set YAML file location as Env
ENV CONFIG_PATH=/app/config/data.yaml

# Set up work dir
WORKDIR /app/src

# To make container always executable
CMD ["tail","-f","/dev/null"]