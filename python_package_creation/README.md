Best working option is to use:
https://github.com/codrsquad/setupmeta

It's an add-on to your setup.py that only needs "setup_requires=["setupmeta"]" like in:

```
from setuptools import setup
setup(
    name="direct",
    setup_requires=["setupmeta"],
)
```

This way you can write:

- python setup.py explain


(after installing the package requirements)
python3 -mvenv .venv
.venv/bin/pip install -U pip setuptools wheel
.venv/bin/pip install -e .
.venv/bin/python setup.py --version
.venv/bin/cli2 --help

You need to paly a bit with the tagging to work but in essence it's:
1) git tag -a v1.0.0
2) python setup.py version --bump patch --commit


Worked best for me:
setup(
    versioning="post",
    ...
)
- python setup.py version --bump patch --commit
- python setup.py version --bump minor --commit
- python setup.py version --bump major --commit


The data for "python setup.py explain" is taken form __init__.py of the libraries folder:
"""
A package implemented by one direct (not under src/) module folder
keywords: direct, package
author: Someone someone@example.com
"""

__version__ = "1.0.0"
__url__ = "https://github.com/codrsquad/simple"
__download_url__ = "https://github.com/codrsquad/simple/archive/{version}.tar.gz"


def main():
    pass

[https://github.com/codrsquad/setupmeta/blob/master/examples/direct/direct/__init__.py]


From: https://medium.com/analytics-vidhya/how-to-create-a-python-library-7d5aea80cc3f

In your environment, make sure you have pip installed wheel, setuptools and twine. We will need them for later to build our Python library.
- pip install wheel
- pip install setuptools
- pip install twine


Running:
- python setup.py pytest
will execute all tests stored in the ‘tests’ folder.
!!!you need to install pytest-runner and pytest to make this work!!!

Step 5: Build your library
Now that all the content is there, we want to build our library. Make sure your present working directory is /path/to/mypythonlibrary (so the root folder of your project). In your command prompt, run:
- python setup.py bdist_wheel

Your wheel file is stored in the “dist” folder that is now created. You can install your library by using:
- pip install /path/to/wheelfile.whl