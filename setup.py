# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages

def get_version(relpath):
  """Read version info from a file without importing it"""
  from os.path import dirname, join
  root = dirname(__file__)
  for line in open(join(root, relpath), "rb"):
    # encoding is not passed to open() parameter, because
    # it is incompatible with Python 2
    line = line.decode("utf-8")
    if "__version__" in line:
      if '"' in line:
        return line.split('"')[1]

# readme_file = open("README_PYPI.rst", "r")
VERSION = get_version("pokedex/main.py")
# README = readme_file.read()
# readme_file.close()

setup(
    name="pokedex-cli",
    packages=find_packages(),
    version=VERSION,
    description="Pokédex CLI",
    #long_description=README,
    author="Ujjwal",
    author_email="ujj.1729@gmail.com",
    url="https://github.com/ujjwal-singh/pokedex-cli",
#    download_url="https://github.com/ujjwal-singh/pokedex-cli/tarball/" + VERSION,
    keywords=["pokedex", "pokemon", "terminal", "cli"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7"
    ],
    install_requires=["Pillow", "requests", "progressbar2", "click"],
    extras_require={
        "test": ["pytest"]
    },
    entry_points={
        "console_scripts": [
            "pokedex = pokedex.main:pokedex"
        ]
    },
    package_data={
        "pokedex": ["resources/icons/*.png", "resources/voices/*.wav", "resources/veekun-pokedex.sqlite.gz"] 
    }
)
