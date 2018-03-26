import os
from os.path import dirname, abspath, join

# Get the path of manage.py
path = join(dirname(dirname(abspath(__file__))), 'manage.py')

os.system('pythonw ' + path + ' runserver')