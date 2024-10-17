# Import necessary functions from setuptools
'''
setuptool is a Python package designed to facilitate the packaging, distribution, and installation of Python software. It extends the packaging capabilities provided by the distutils standard library, offering additional features and functionalities for developers to easily build and distribute their Python projects
'''
from setuptools import setup, find_packages

# Import the version of the package from the clausewitz module
'''
The __version__ variable is defined in the __init__.py file of the clausewitz package. By importing it here, we can dynamically set the version of the package during the setup process.
'''
from clausewitz import __version__

# List of runtime dependencies required by the package
requirements = [
    'cached-property',  # A decorator for caching properties in classes.
    'returns-decorator',  # Presumably a custom or third-party decorator for handling function returns.
]

# List of extra dependencies for testing
extra_test = [
    'flake8',  # Tool for style guide enforcement.
    'flake8-commas',  # Plugin for flake8 to enforce comma usage.
    'flake8-print',  # Plugin for flake8 to check for print statements.
    'flake8-quotes',  # Plugin for flake8 to enforce quote style.

    'pytest>=4',  # Testing framework, version 4 or newer.
    'pytest-runner>=4',  # Adds pytest support to setuptools.
    'pytest-cov>=2',  # Plugin for pytest to measure code coverage.
]
extra_dev = extra_test  # Development dependencies are the same as test dependencies.

# List of extra dependencies for continuous integration
extra_ci = extra_test + [
    'coverage==4.*',  # Tool for measuring code coverage, version 4.
    'python-coveralls',  # Tool for integrating coverage data with Coveralls.io.
]

# Configuration for setuptools
setup(
    name='pypdx-clausewitz',  # Name of the package.
    version=__version__,  # Version of the package, imported from clausewitz module.
    packages=find_packages(),  # Automatically find and include all packages in the project.
    install_requires=requirements,  # Runtime dependencies.
    extras_require={  # Optional dependencies that can be installed for specific setups.
        'test': extra_test,
        'dev': extra_dev,
        'ci': extra_ci,
    },
    # The setup function would typically include more parameters, such as author, description, etc.
)