from distutils.core import setup


setup(
    name='enumerable',
    packages=['enumerable'],
    version='0.2',
    install_requires=['future'],
    description='An improvement on Python\'s map, filter and reduce.',
    author='Ryan "Brent" Taylor',
    author_email='btaylor@fuzzylogicstudios.com',
    url='https://github.com/brenttaylor/enumerable',
    download_url='https://github.com/brenttaylor/enumerable/archive/release-0.2.tar.gz',
    keywords=['functools', 'map', 'filter', 'reduce'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7'
        ],
)
