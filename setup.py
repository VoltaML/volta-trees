from setuptools import find_packages, setup

setup(
    name="voltatrees",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=["llvmlite>=0.36", "numpy"]
)