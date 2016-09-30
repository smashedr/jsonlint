from distutils.core import setup
import py2exe

setup(
    console=[{'script': "jsonlint.py"}],
    options={
        'py2exe': {
            'bundle_files': 1,
            'compressed': True
        }
    },
    zipfile=None,
)
