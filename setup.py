"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="fakernaija",
    version="1.0.0",
    description="A Python package to generate random Nigerian-specific data for you.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pythonian/fakernaija",
    author="Seyi Pythonian",
    author_email="seyipythonian@gmail.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    keywords="faker data generator mock nigeria naija test",
    packages=find_packages(),
    package_data={"": ["*.json"]},
    install_requires=[
        "click==8.1.7",
    ],
    entry_points={
        "console_scripts": [
            "naija=fakernaija.cli:cli",
        ],
    },
    python_requires=">=3.10, <4",
    project_urls={
        "Bug Reports": "https://github.com/Pythonian/fakernaija/issues",
        "Source": "https://github.com/Pythonian/fakernaija",
    },
)
