:: If you're using Windows, you can make this batch file run when you log into your account.
:: This is very handy because you can forgot about having to manually run BrowserBoard from the console.

:: *How to setup with Task Scheduler*
:: To make this run when you login, open 'Task Scheduler'.
:: Then click 'Create Task...' (Fill in the details as you see fit)
:: Go to the 'Triggers' tab, and click 'New'.
:: 	'Begin the task': 'At log on'
:: Press 'Ok'
:: Now go to the 'Actions' tab and press 'New'.
::	'Program/Script': (locate this batch file)
::	'Start in (optional)': (locate the folder which contains this batch file)
:: Press 'Ok' twice.

@echo off
start pythonw manage.py runserver