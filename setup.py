from setuptools import find_packages
from setuptools import setup

REQUIRED_PACKAGES = ['distance', 'numpy', 'six', 'pillow']
VERSION = '0.7.4.02'
try:
    import pypandoc
    README = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    README = open('README.md').read()


setup(
    name='aocr',
    url='https://github.com/laldev/attention-ocr',
    download_url='https://github.com/laldev/attention-ocr/archive/{}.tar.gz'.format(VERSION),
    author='jithin',
    author_email='jithinlaldev@gmail.com',
    version=VERSION,
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description=('''Optical character recognition model '''
                 '''for Tensorflow based on Visual Attention.'''),
    long_description=README,
    entry_points={
        'console_scripts': ['aocr=aocr.__main__:main'],
    }
)
