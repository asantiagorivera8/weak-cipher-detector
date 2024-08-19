from setuptools import setup, find_packages

setup(
    name="weak-cipher-detector",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "cryptography",
    ],
    entry_points={
        "console_scripts": [
            "weak-cipher-detector=weak_cipher_detector:main_menu",
        ],
    },
    author="Angel D. Santiago Rivera",
    author_email="adsr.20@gmail.com",  # Replace with your actual email
    description="A tool to detect weak ciphers in SSL/TLS certificates",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/asantiagorivera8/weak-cipher-detector",  # Replace with your actual GitHub repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
