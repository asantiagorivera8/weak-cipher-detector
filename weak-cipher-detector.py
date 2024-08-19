import ssl
import socket
import os
from datetime import datetime
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print("=" * 50)
    print("       Weak Cipher Detector in Certificates")
    print("          Author: Angel D. Santiago Rivera")
    print("=" * 50)
    print("TechBiz".rjust(48))
    print("\n")

def create_banner(message, is_secure):
    color = GREEN if is_secure else RED
    width = len(message) + 4
    border = f"+{'-' * (width - 2)}+"
    return f"""
{color}{border}
|  {message}  |
{border}{RESET}
"""

def get_server_certificate(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
            der_cert = secure_sock.getpeercert(binary_form=True)
            return x509.load_der_x509_certificate(der_cert, default_backend())

def is_weak_cipher(cipher_suite):
    weak_ciphers = [
        'RC4', 'DES', '3DES', 'MD5', 'SHA1',
        'NULL', 'EXPORT', 'anon'
    ]
    return any(weak in cipher_suite for weak in weak_ciphers)

def analyze_certificate(hostname):
    try:
        cert = get_server_certificate(hostname)
        
        print(f"\nAnalyzing certificate for: {hostname}\n")
        
        is_secure = True
        warnings = []

        # Check certificate validity
        now = datetime.now()
        if cert.not_valid_after < now:
            is_secure = False
            warnings.append("Certificate has expired")
        elif cert.not_valid_before > now:
            is_secure = False
            warnings.append("Certificate is not yet valid")
        
        # Check key size
        public_key = cert.public_key()
        key_size = public_key.key_size
        if isinstance(public_key, (rsa.RSAPublicKey, dsa.DSAPublicKey)):
            if key_size < 2048:
                is_secure = False
                warnings.append(f"Weak key size: {key_size} bits (should be at least 2048 bits)")
        
        # Check signature algorithm
        signature_algorithm = cert.signature_algorithm_oid._name
        if 'sha1' in signature_algorithm.lower():
            is_secure = False
            warnings.append(f"Weak signature algorithm: {signature_algorithm}")
        
        # Check cipher suite
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
                cipher = secure_sock.cipher()
                if is_weak_cipher(cipher[0]):
                    is_secure = False
                    warnings.append(f"Weak cipher detected: {cipher[0]}")
        
        # Print security assessment
        if is_secure:
            message = f"The website {hostname} appears to be SECURE"
            print(create_banner(message, True))
            print("It should be safe to enter your data and navigate on this site.")
        else:
            message = f"The website {hostname} may NOT BE SECURE"
            print(create_banner(message, False))
            print("Exercise caution when entering sensitive data on this site.")
            print(f"\n{BOLD}Warnings:{RESET}")
            for warning in warnings:
                print(f"- {warning}")
        
        # Print additional details for interested users
        print(f"\n{BOLD}Additional Details:{RESET}")
        print(f"Certificate Version: {cert.version}")
        print(f"Serial Number: {cert.serial_number}")
        print(f"Issuer: {cert.issuer}")
        print(f"Subject: {cert.subject}")
        print(f"Not Valid Before: {cert.not_valid_before}")
        print(f"Not Valid After: {cert.not_valid_after}")
        print(f"Key Size: {key_size} bits")
        print(f"Signature Algorithm: {signature_algorithm}")
        
    except ssl.SSLError as e:
        print(f"{RED}SSL Error: Unable to establish a secure connection to {hostname}{RESET}")
        print(f"Details: {str(e)}")
    except socket.gaierror:
        print(f"{RED}Error: Unable to resolve hostname {hostname}{RESET}")
    except socket.error as e:
        print(f"{RED}Connection Error: Unable to connect to {hostname}{RESET}")
        print(f"Details: {str(e)}")
    except Exception as e:
        print(f"{RED}Unexpected error analyzing the certificate: {str(e)}{RESET}")

def main_menu():
    while True:
        print_header()
        print("1. Analyze website security")
        print("2. Exit")
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            hostname = input("Enter the domain name to analyze (e.g., example.com): ")
            analyze_certificate(hostname)
            input("\nPress Enter to continue...")
        elif choice == '2':
            print("Thank you for using the Weak Cipher Detector. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
