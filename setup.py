import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TauLidarCommon",
    version="0.0.1",
    author="Onion Corporation",
    author_email="hello@onion.io",
    description="Tau Lidar Common package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OnionIoT/tau-lidar-common",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.1',
)
