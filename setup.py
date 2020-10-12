from setuptools import setup, find_packages


setup(
    name="GA",
    version="0.1",
    author="lipo",
    author_email="lipo8081@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"}
)
