from pathlib import Path
from setuptools import setup, find_packages

version = [
    line
    for line in Path("sphinxcontrib_svg_links/__init__.py").read_text().split("\n")
    if "__version__" in line
]
version = version[0].split(" = ")[-1].strip('"')

with open("./README.md", "r") as ff:
    readme_text = ff.read()

setup(
    name="sphinxcontrib-svg-links",
    version=version,
    description="A sphinx extension for linking to URIs and sphinx labels from SVG graphics.",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    author="Volker Jaenisch",
    author_email="volker.janeisch@inqbus.de",
    url="https://github.com/sphinxcontrib-svg-links",
    project_urls={"Documentation": "https://sphinxcontrib-svg-links.readthedocs.io"},
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "sphinx>6,<8",
    ],
    extras_require={
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Sphinx :: Extension",
    ],
    keywords="sphinx html SVG links diagramm URI",
)