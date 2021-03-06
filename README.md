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
 $ cd vest
 $ virtualenv --python=/usr/bin/python3 .ve
 $ source .ve/bin/activate
 $ pip install -r requirements.txt
```

## Run

```
 $ systemctl start postgresql
 $ systemctl start redis
 $ cd vest
 $ python manage.py migrate
 $ python manage.py runserver
```

## Create a SuperUser

```
 $ # In ./vest/ folder
 $ python manage.py createsuperuser
```

## Setup with docker-compose

Alternatively you can launch the app into a docker just like that:

```
docker-compose up -d
```

You of course need to install `docker` and `docker-compose` and need to setup your settings for your docker. For instance:

```
{
    'ENGINE': 'django.contrib.gis.db.backends.postgis',
    'NAME': 'postgres',
    'USER': 'postgres',
    'PORT': '5432',
    'HOST': 'db',
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
        "ROUTING": "realtime.routing.channel_routing",
    },
}
```



