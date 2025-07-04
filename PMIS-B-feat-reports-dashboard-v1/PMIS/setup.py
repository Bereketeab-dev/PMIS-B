from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="construction_pmis",
    version="0.0.1",
    description="Construction Project Management Information System",
    author="[Your Name/Organization]",
    author_email="[your.email@example.com]",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=requirements,
)
