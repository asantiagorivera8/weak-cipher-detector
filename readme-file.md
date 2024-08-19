# Weak Cipher Detector

Weak Cipher Detector is a tool designed to analyze SSL/TLS certificates of websites and detect weak ciphers and other potential vulnerabilities. This tool is essential for cybersecurity professionals, system administrators, and anyone interested in ensuring the security of web communications.

## Author

Angel D. Santiago Rivera

## Features

- Analyzes SSL/TLS certificates of websites
- Detects weak ciphers and vulnerable encryption methods
- Provides information about certificate validity, issuer, and subject
- Checks for weak key sizes and signature algorithms

## Installation

To install Weak Cipher Detector, follow these steps:

1. Ensure you have Python 3.6 or higher installed on your system.

2. Clone this repository:
   ```
   git clone https://github.com/yourusername/weak-cipher-detector.git
   ```

3. Navigate to the project directory:
   ```
   cd weak-cipher-detector
   ```

4. Install the package:
   ```
   pip install .
   ```

## Usage

After installation, you can run the Weak Cipher Detector from the command line:

```
weak-cipher-detector
```

Follow the on-screen prompts to analyze website certificates:

1. Choose option 1 to analyze a website certificate.
2. Enter the domain name you want to analyze (e.g., example.com).
3. Review the analysis results.

## Requirements

- Python 3.6+
- cryptography library

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions to the Weak Cipher Detector are welcome! Please feel free to submit a Pull Request.

## Disclaimer

This tool is for educational and informational purposes only. Always ensure you have permission before scanning websites you do not own or operate.
