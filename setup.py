from setuptools import setup, find_packages

setup(
    name="magicMahler",               # Name of your package
    version="1.0",                  # Version of your package
    packages=find_packages(),         # Automatically find packages
    install_requires=[],              # List of dependencies (if any)
    include_package_data=True,        # Include package data specified in MANIFEST.in
    description="A package for polytopes and related computations.",  # Short description
    author="vmastr",               # Your name
    author_email="",  # Your email
    url="https://github.com/yourusername/magicMahler",  # Optional: URL to your project's homepage or repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
