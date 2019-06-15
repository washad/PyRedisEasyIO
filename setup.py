import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrediseasyio",
    version="0.0.7",
    author="Steve Jackson",
    author_email="washad@gmail.com",
    description="A set of tools for simplifying reading and writing of single values to/from Redis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/washad/PyRedisEasyIO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
