## Installation of pre-requisites

1. Python3
1. virtualenv
1. PostgreSQL

If you have all the pre-requisites installed, skip this step and go to next step

### Install virtualenv

```sh
sudo apt-get install virtualenv
virtualenv --version
```

### Install PostgreSQL

```sh
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install postgresql postgresql-contrib
psql --version
```

## Setup PostgreSQL database

1. create a new user if you do not want to use existing users
1. give new user superuser role
1. create new database 'tkdc' with the chosen user as owner

```sh
# enter postgresql cli
sudo su postgres
psql
```

```sql
CREATE USER <username> WITH PASSWORD <password>;

/* give the new user superuser role */
ALTER USER <username> WITH SUPERUSER;

/* create new tkdc database with one of the users as owner */
CREATE DATABASE mess_management WITH OWNER=<username>;
```

## Project Setup

```sh

# create virtual environment with python3.8 as default python and activate it
virtualenv .venv
source .venv/bin/activate

# install api dependecies
pip install -r requirements.txt

# copy example env containing necessary environment variables to .env
cp env.example .env
```

open `.env` and input values of following variables

```env
DJANGO_SECRET_KEY
DATABSE_OWNER
DATBASE_PASSWORD
```

complete setup with the following commands

```sh
# migrate database with the application models
python manage.py migrate

# create superuser
python manage.py createsuperuser

# run server
python manage.py runserver
```
