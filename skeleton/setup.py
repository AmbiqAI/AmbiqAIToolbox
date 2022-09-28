#!/usr/bin/env python3
"""
CHANGE_ME module.
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# load version vars
# pylint: disable=exec-used,consider-using-with
exec(open("python/version.py", "r", encoding="utf-8").read())

install_requires = []

extra_deps = {
    "dev": [
        "pre-commit>=2.19.0",
        "black>=22.3.0",
        "pyright>=1.1.264",
        "isort>=5.10.0",
        "pylint>=2.13.8",
        "pytest>=7.1.2",
    ]
}

setup(
    name="CHANGE_ME",
    version=__version__,  # type: ignore pylint: disable=undefined-variable
    author="Ambiq AI",
    description="CHANGE_ME reference model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ambiqai/CHANGE_ME",
    packages=["CHANGE_ME"],
    package_dir={"CHANGE_ME": "python"},
    install_requires=install_requires,
    extras_require=extra_deps,
)
