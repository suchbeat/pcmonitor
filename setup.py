from setuptools import setup

setup(
    name='pcmonitor',
    version='0.0.2',
    description='HTOP Python package',
    author='suchbeat',
    author_email='s.u.chbeat@gmail.com',
    url='https://github.com/suchbeat/pcmonitor.git',
    license='MIT',
    packages=['pcmonitor'],
    install_requires=['psutil'],
    scripts=['.bin/pcmonitor'],
)
