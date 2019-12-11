# Flask-Vue SPA

## Build using following versions
+ Docker
    + version 18.03.1-ce, build 9ee9f40
+ Docker-compose
    + version 1.21.1
+ Postgres
    + version postgres:10
## Setup
``` bash
# First run
docker-compose build

# Then 
docker-compose up

# To rebuild
docker-compose up --build

```

## Usage
1. Navigate to http://localhost:8080/
    + That will bring up the registration component
2. Once registerd you will be redirected to the login page
    + http://localhost:8080/#/login
3. Enter your credentials
    + You will be redirected to http://localhost:8080/#/keys
    + There you can add and remove keys associated with your account
## TODO
+ Fix pytest runtime problem
