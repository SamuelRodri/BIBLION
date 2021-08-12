from distutils.core import setup
import py2exe, sys, os
#...
#...
sys.argv.append('py2exe')

DATA=[('imageformats',['C:\\Users\\Samuel\\Desktop\\PROYECTOS\\BIBLION\\BIBLION v1.1.1'    ])]

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True,"includes":["sip"]}},
    windows = [{'script': "BIBLION.pyw"}],
    zipfile = None,
    data_files = DATA,
)