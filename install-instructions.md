# Installation Instructions for Weak Cipher Detector

This document provides step-by-step instructions to install the Weak Cipher Detector tool on various systems.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)
- git

## Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/asantiagorivera8/weak-cipher-detector.git
   ```

2. Navigate to the project directory:
   ```
   cd weak-cipher-detector
   ```

3. Install the package:
   ```
   pip3 install .
   ```

   Note: If you want to install it system-wide, use:
   ```
   sudo pip3 install .
   ```

4. After installation, you should be able to run the tool using:
   ```
   weak-cipher-detector
   ```

## Troubleshooting

If you encounter any issues during installation, try the following:

1. Ensure you have the latest version of pip:
   ```
   pip3 install --upgrade pip
   ```

2. If you get an error related to the `cryptography` library, install these dependencies:
   ```
   sudo apt install build-essential libssl-dev libffi-dev python3-dev
   ```
   Then try the installation again.

3. If the `weak-cipher-detector` command is not found after installation:
   - Check if the package is installed:
     ```
     pip3 list | grep weak-cipher-detector
     ```
   - If it's installed but the command doesn't work, try adding this to your `~/.bashrc` or `~/.zshrc`:
     ```
     export PATH=$PATH:$HOME/.local/bin
     ```
     Then restart your terminal or run `source ~/.bashrc` (or `~/.zshrc`).

4. If you're still having issues, you can run the script directly:
   ```
   python3 /path/to/weak-cipher-detector.py
   ```
   Replace `/path/to/` with the actual path to the script.

## Updating

To update to the latest version:

1. Navigate to the project directory:
   ```
   cd weak-cipher-detector
   ```

2. Pull the latest changes:
   ```
   git pull
   ```

3. Reinstall the package:
   ```
   pip3 install . --upgrade
   ```

## Uninstallation

To uninstall the tool:
```
pip3 uninstall weak-cipher-detector
```

If you encounter any problems during installation or usage, please open an issue on the GitHub repository.
