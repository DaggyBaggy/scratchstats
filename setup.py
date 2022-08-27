from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='ScratchStats',
    url='https://github.com/DaggyBaggy/scratchstats',
    author='DaggyBaggy',
    author_email='NONE',
    packages=['scratchstats'],
    install_requires=['numpy', 'requests'],
    version='0.0.1',
    license='MIT',
    description='An easy way to access ScratchDB API',
    long_description=open('README.md').read(),
)
