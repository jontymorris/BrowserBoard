# BrowserBoard
A central homepage for your favourite media

## What is BrowserBoard
BrowserBoard is the homepage you never had.
It will keep track of your favorite things and will even alert you to any updates.

## Getting setup
In order to run BrowserBoard, you will need to have an installation of Python 3, Django and BeautifulSoup 4.

You can install Python from the the [official website](https://www.python.org).

An easy way to install the required libraries is via PyPI.
```
pip install -r requirements.txt
```

Next, you will now need to `cd` into the BrowserBoard directory.

If you are running BrowserBoard for the first time, you will need to execute the following commands.
```
python manage.py migrate
```

Finally, whenever you want to start BrowserBoard, enter the following command.
(Window's users can look at the 'start.bat' for an automated startup)
```
python manage.py runserver
```

Now that everything is setup, it is also recommended that you make BrowserBoard your internet browser's homepage :)

## Supported sites
- [MangaPanda.com](https://www.mangapanda.com/)
