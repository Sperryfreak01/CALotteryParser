from distutils.core import setup
import py2exe
import requests.certs

setup(console=['Downloader.py'],
        data_files = '',
        options = {
            'py2exe': {
            'packages': ['csv', 'StringIO', 'requests']
        }
    }
)