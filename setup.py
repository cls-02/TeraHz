import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="terahz", # Replace with your own username
    version="1.0.0",
    author="Kristjan Komloši",
    author_email="kristjan.komlosi@gmail.com",
    description="Low cost spectrometry webapp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cls-02/TeraHz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    )
