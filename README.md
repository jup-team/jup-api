# jup-api

## up and running the project locally
The configuration below is a step-by-step to set your dev env running the jup api connected to a postgres.


### docker-compose to build the containers and configurations
`docker-compose build`

### creating super user
`sudo docker-compose run app sh -c "python3 manage.py createsuperuser"`


### creating new apps in the project

suppose you want to create a /candidates app in the project:

`sudo docker-compose run app sh -c "django-admin startapp candidates"`

### the .env.dev file

I added by default some variables for db, you can go with it. But also you can change if you want to.

### adding new libs

if you add a new lib, follow the steps:
  1. add the lib in requirements.txt
  2. run `docker-compose run --build`
