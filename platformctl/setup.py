from setuptools import setup, find_packages

setup(
    name="platformctl",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "typer[all]"
    ],
    entry_points={
        "console_scripts": [
            "platformctl=cli.main:app"
        ]
    },
)
