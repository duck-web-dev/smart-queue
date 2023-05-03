from setuptools import setup, find_packages

setup(
    name='smart_queue',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
    ],
    author='Duck Dev.',
    description='SmartQueue library for handling sync tasks, like single-threaded DB writes or other I/O with possible race conditions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/duck-web-dev/smart_queue',
    license='MIT',
    classifiers=[
    ],
)