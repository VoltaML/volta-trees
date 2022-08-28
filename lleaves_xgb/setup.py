from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))

setup(
    name="lleaves_xgb",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.7",
    install_requires=["llvmlite>=0.36", "numpy"],
)
