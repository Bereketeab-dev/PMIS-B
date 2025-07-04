from setuptools import setup, find_packages

setup(
    name='pmis',
    version='0.0.1',
    description='Construction PMIS App for ERPNext',
    author='Your Name or Company',
    author_email='your@email.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe'],
)
