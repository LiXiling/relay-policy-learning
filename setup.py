from setuptools import find_packages, setup

setup(
    name="adept_envs",
    version="0.1",
    package_dir={"": "adept_envs"},
    packages=find_packages(where="adept_envs"),
)
