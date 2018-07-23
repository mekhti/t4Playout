from setuptools import setup

setup(
    name='t4Playout',
    version='0.1',
    packages=['conf', 'Playout', 'Playout.Apps', 'Playout.Admin', 'Playout.Tests', 'Playout.Views', 'Playout.Models',
              'Playout.management', 'Playout.management.commands', 'Playout.migrations', 't4Playout'],
    url='https://www.mbsys.tv',
    license='MIT',
    author='Mehdi Mammadov',
    author_email='mekhti@gmail.com',
    description='Client for CasparCG '
)
