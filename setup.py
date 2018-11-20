
from setuptools import setup

setup(
    name='robot',
    version='1.0.1',
    description='Hacked robot machine Skill',
    author='Snips Labs',
    url='',
    download_url='',
    license='MIT',
    install_requires=['pyserial', 'configparser','netaddr', ' pycryptodome'],
    test_suite="tests",
    keywords=['snips', 'robot'],
    packages=['robot'],
    package_data={'robot': ['Snipsspec']},
    include_package_data=True
)