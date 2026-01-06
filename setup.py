from setuptools import setup, find_packages

setup(
    name="brain_tumor_detection",
    version="0.0.1",
    author="Suvarna Gawali",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
