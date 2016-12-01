from distutils.core import setup

setup(
    name = 'pcmonitor',
    version = '0.0.1',
    description = 'HTOP Python package',
    author = 'suchbeat',
    author_email = 's.u.chbeat@gmail.com',
    url = 'https://github.com/zaiste/zaiste-py',
    py_modules=['pcmonitor'],
    install_requires=[
        # list of this package dependencies
    ],
    entry_points='''
        [console_scripts]
        zaiste=zaiste:cli
    ''',
)
