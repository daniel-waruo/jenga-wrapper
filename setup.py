import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-jenga",  # Replace with your own username
    version="0.0.1",
    author="Daniel Waruo",
    author_email="waruodaniel@example.com",
    description="Python wrapper for the JENGA api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daniel-waruo/jenga-wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)