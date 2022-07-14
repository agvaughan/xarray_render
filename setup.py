"""Python setup.py for xarray_render package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("xarray_render", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="xarray_render",
    version=read("xarray_render", "VERSION"),
    description="Awesome xarray_render created by agvaughan",
    url="https://github.com/agvaughan/xarray_render/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="agvaughan",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["xarray_render = xarray_render.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
