import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="is-natural-number",
    version="1.0.0",
    author="Adam Zerella",
    author_email="hello@adamzerella.com",
    description="Check if a value is a natural number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamzerella/is-natural-number",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)