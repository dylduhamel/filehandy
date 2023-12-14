import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filehandy",
    version="0.0.1",
    author="Dylan Duhamel",
    author_email="duhadm19@alumni.wfu.edu",
    description="filehandy is a Python library that offers a set of tools to make file input and output operations more accessible and efficient.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dylduhamel/filehandy",
    packages=setuptools.find_packages(),
    install_requires=[
        # Common dependencies here
        'pywin32; platform_system=="Windows"'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)