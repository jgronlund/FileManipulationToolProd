#!/usr/bin/env bash
set -e  # exit on first error
set -u  # exit on undefined variables
set -o pipefail

# ---------------------------------------------------------
# Filetool Installer
# Installs the filetool CLI from a .deb package
# ---------------------------------------------------------

# Function to show usage
usage() {
    echo "Usage: $0 path/to/filetool_*.deb"
    exit 1
}

# Check arguments
if [ "$#" -ne 1 ]; then
    usage
fi

DEB_FILE="$1"

if [ ! -f "$DEB_FILE" ]; then
    echo "Error: File '$DEB_FILE' does not exist."
    exit 1
fi

echo "Installing Filetool from: $DEB_FILE"

# Update package list
sudo apt update

# Install dependencies
sudo apt install -y python3 python3-pip python3-setuptools

# Install the .deb package
sudo dpkg -i "$DEB_FILE" || sudo apt -f install -y

echo "Filetool installed successfully!"
echo "You can now run it with the command: filetool"
