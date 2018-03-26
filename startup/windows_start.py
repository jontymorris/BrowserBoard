import os

# Remove 'startup' from dirname
DIR_PARTS = os.path.dirname(os.path.realpath(__file__)).split("\\")
DIR = ""
for i in range(0, len(DIR_PARTS)-1):
	DIR += DIR_PARTS[i] + "\\"

os.system("pyw " + DIR + "manage.py runserver")
