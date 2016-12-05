# VEST Server

## Dependances

* postgresql
* postgis
* gdal
* python-psycopg2 

## Setup the PostGreSQL database

[Read Here](https://wiki.archlinux.org/index.php/PostgreSQL)

Also don't forget to setup your own 'DATABASES' setting in 
_vest/vest/settings.py_ with your database 'NAME' and your database 'USER'

Import the borders data:

```
$ python manage.py shell
Python 3.5.2 (default, Nov  7 2016, 11:31:36) 
[GCC 6.2.1 20160830] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from world import load
>>> load.run()
```

## Setup

```
 $ git clone https://github.com/vest-thermostat/server
 $ cd server
 $ virtualenv --python=/usr/bin/python3 .ve
 $ source .ve/bin/activate
 $ pip install -r requirements.txt
```

## Run

```
 $ cd vest
 $ python manage.py migrate
 $ python manage.py runserver
```

## Create a SuperUser

```
 $ # In ./vest/ folder
 $ python manage.py createsuperuser
```
