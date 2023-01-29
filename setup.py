from setuptools import setup, find_packages

setup(
    name='affinity',
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
        "rich",
    ],
    entry_points ={
        'console_scripts': [
            "affinity = affinity.__main__:main"
        ]
    }
)