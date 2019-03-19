import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magpy",
    version="0.0.3",
    author="Rhys Goodall",
    author_email="reag2@cam.ac.uk",
    description="Chemical Feature Look-up",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/comprhys/magpy",
    packages=setuptools.find_packages(),
    package_data={'magpy': ['tables/*.csv']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
