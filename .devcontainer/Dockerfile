FROM ubuntu:latest

# Install TypeScript
RUN apt-get update && \
  apt-get install -y nodejs npm && \
  npm install -g typescript

# Install Python
RUN apt-get install -y python3 python3-pip

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Install OpenAI
RUN pip3 install openai

# Install Google Cloud SDK
RUN apt-get install -y curl && \
  export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
  echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
  apt-get update && \
  apt-get install -y google-cloud-sdk

# Install Firebase CLI and Firestore
RUN curl -sL https://firebase.tools | bash

# Install MongoDB
RUN apt-get install -y mongodb

# Install Redis
RUN apt-get install -y redis-server

# Install PostgreSQL
RUN apt-get install -y postgresql

# Install Neo4j
RUN apt-get install -y neo4j

# Add workspace app folder
WORKDIR /app

# Expose ports
EXPOSE 3000

# Enable access to the local filesystem
VOLUME ["/app"]

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' myuser
USER myuser