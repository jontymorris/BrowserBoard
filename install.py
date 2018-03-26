from sys import platform as _platform
from winreg import *
import os

class Installer:

	def __init__(self):
		print("="*40 + "\n" + "\tSetting Up BrowserBoard\n" + "="*40 + "\n")

		# Migrate tables
		print("Migrating Tables...")
		migrate_output = os.popen('pyw manage.py migrate').read()
		if migrate_output != "":
			print("\t" + migrate_output)

		# Run at startup
		while True:
			print("Would you like BrowserBoard to automatically run at startup?")
			option = input("y/n: ").lower()
			if option == "y" or option == "yes":
				
				# Linux
				if _platform == "linux" or _platform == "linux2":
			   		self.linux_startup()

				# MAC OS X
				elif _platform == "darwin":
					self.mac_startup()

				# Windows
				elif _platform == "win32" or "win64":
					self.windows_startup()
				break

			elif option == "n" or option == "no":
				break
			else:
				print("\tbad value!\n")

		# Done
		print("Finished!")

	def windows_startup(self):
		reg = OpenKey(HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Run',0, KEY_ALL_ACCESS)
		value = os.path.dirname(os.path.realpath(__file__)) + "\startup\start_server.pyw"
		with reg:
			if '%' in value:
				var_type = REG_EXPAND_SZ
			else:
				var_type = REG_SZ
				SetValueEx(reg, 'BrowserBoard', 0, var_type, value)

	def linux_startup(self):
		print("Sorry, Linux isn't supported at the moment")

	def mac_startup(self):
		print("Sorry, Mac isn't supported at the moment")


installer = Installer()			