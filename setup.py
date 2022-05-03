import re
from codecs import open
from glob import glob
from itertools import chain
from os import path

from setuptools import find_packages, setup
version="0.1.0"

setup(
    name="fast-click",
    version=version,
    description="fast-click",
    license="Apache Software License (Apache 2.0)",
    url="https://github.com/noklam/fast-click",
    python_requires=">=3.7, <3.11",
    author="noklam",
    entry_points={"console_scripts": ["fast-click = fast_click:main"]},
    keywords="pipelines, machine learning, data pipelines, data science, data engineering",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)