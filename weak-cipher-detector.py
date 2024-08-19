import ssl
import socket
import os
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, dsa, ec

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print("=" * 50)
    print("       Weak Cipher Detector in Certificates")
    print("          Author: Angel D. Santiago Rivera")
    print("=" * 50)
    print("TechBiz".rjust(48))  # Align "TechBiz" to the right
    print("\n")

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
        
        print(f"Analyzing certificate for: {hostname}")
        print(f"Version: {cert.version}")
        print(f"Serial number: {cert.serial_number}")
        print(f"Issuer: {cert.issuer}")
        print(f"Subject: {cert.subject}")
        print(f"Not valid before: {cert.not_valid_before}")
        print(f"Not valid after: {cert.not_valid_after}")
        
        public_key = cert.public_key()
        key_size = public_key.key_size
        
        if isinstance(public_key, (rsa.RSAPublicKey, dsa.DSAPublicKey)):
            if key_size < 2048:
                print(f"ALERT: Weak key size ({key_size} bits)")
            else:
                print(f"Key size: {key_size} bits")
        elif isinstance(public_key, ec.EllipticCurvePublicKey):
            print(f"Elliptic curve: {public_key.curve.name}")
        
        signature_algorithm = cert.signature_algorithm_oid._name
        if 'sha1' in signature_algorithm.lower():
            print(f"ALERT: Weak signature algorithm: {signature_algorithm}")
        else:
            print(f"Signature algorithm: {signature_algorithm}")
        
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
                cipher = secure_sock.cipher()
                if is_weak_cipher(cipher[0]):
                    print(f"ALERT: Weak cipher detected: {cipher[0]}")
                else:
                    print(f"Cipher: {cipher[0]}")
        
    except Exception as e:
        print(f"Error analyzing the certificate: {str(e)}")

def main_menu():
    while True:
        print_header()
        print("1. Analyze website certificate")
        print("2. Exit")
        choice = input("\nSelect an option: ")
        
        if choice == '1':
            hostname = input("Enter the domain name to analyze: ")
            analyze_certificate(hostname)
            input("\nPress Enter to continue...")
        elif choice == '2':
            print("Thank you for using the Weak Cipher Detector in Certificates. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
