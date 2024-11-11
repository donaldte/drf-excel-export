from setuptools import setup, find_packages

setup(
    name="drf-excel-export",  # Name of the package
    version="0.1.0",  # Initial version
    description="A tool to export Django REST Framework API documentation in Excel format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Donald Programmeur",  # Replace with your name
    author_email="donaldtedom0@gmail.com",  # Replace with your email
    url="https://github.com/donaldte/drf-excel-export",  # Replace with the actual URL
    packages=find_packages(),
    install_requires=[
        "drf-spectacular",  # For generating API schema
        "openpyxl",         # For handling Excel file generation
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
