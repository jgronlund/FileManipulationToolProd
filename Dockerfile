FROM debian:bookworm

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt update && apt install -y \
    unzip \
    python3 \
    python3-pip \
    apt-utils \
    && rm -rf /var/lib/apt/lists/*

# Create working directory
WORKDIR /app

# Copy zipped Debian package into container
COPY filetool-deb.zip /app/
COPY install_filetool.sh /app/

# Unzip and install the .deb
RUN unzip filetool-deb.zip && \
    dpkg -i *.deb || apt-get install -f -y

# Default to interactive shell
CMD ["/bin/bash"]