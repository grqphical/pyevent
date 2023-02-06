from setuptools import setup, find_packages
from pyevent import __version__

setup(
    name='pyevent',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
)