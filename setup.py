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
    url="<LINK_TO_YOUR_CODE_OR_PRODUCT>",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)