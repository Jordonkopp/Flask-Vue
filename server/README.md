## Server
Flask Server exposing Key Microservice

## Manual Setup

``` bash
# Create virtual env
python3 -m venv env

# Active env
source flask_vue_env/bin/activate

# install dependencies
pip install -r server/requirements.txt

# create DB
python manage.py recreate_db

# build for production with minification
python manage.py runserver

```

## Automated Setup
See README in base directory for docker-compose setup instructions

## TODO
+ Tests
+ Improved error handling
