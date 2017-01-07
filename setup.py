from setuptools import setup
from pypayant import __version__, __author__, __license__


setup(name='pypayant',
      version=__version__,
      description='Python wrapper the Payant API',
      url='https://github.com/Olamyy/pypayant',
      author=__author__,
      author_email='olamyy53@gmail.com',
      license=__license__,
      test_suite='nose.collector',
      tests_require=['nose'],
      install_requires=['requests'],
      packages=['pypayant'],
      zip_safe=False
      )
Setup (

)
