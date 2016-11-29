# VEST Server

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
