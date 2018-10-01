import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gendermeme",
    version="0.0.1",
    url="https://github.com/poorna-kumar/gendermeme-core",
    description="A first open-sourced version of GenderMeme",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'pycorenlp',
        'numpy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
