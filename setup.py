from setuptools import (setup, find_packages)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
      name="phonebook",
      version="0.0.1",
      author="Angel Vargas",
      author_email="angelvargas@outlook.es",
      description="simple phone book rest api",
      long_description=long_description,
      url="https://github.com/angelhvargas/phone-book",
      packages=find_packages(),
      include_package_data=True,
      install_requires=[
          'flask'
      ],
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
)
