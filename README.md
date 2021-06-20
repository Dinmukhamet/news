# News App

News App is a test assessment for DevelopsToday

## Table of Contents

* [Setup](#setup)
* [Documentation](#documentation)
* [Deployment link](#deployment-link)
* [Linting & Formatting](#linting-and-formatting)

## Setup
### Via Docker

Install [docker](https://www.docker.com/get-started) and [docker-compose](https://docs.docker.com/compose/)

After installation run the following command
```bash
docker-compose up -d --no-deps --build
```

And you are good to go


### Without Docker

*The following setup is for Linux users only*

Create virtual environment

```bash
python3 -m venv venv
```

Activate it

```bash
source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip3 install -r requirements.txt
```

Create .env and .db.env files.
Set the environment variables. 
Look at [example](.env.template)


Use `migrate` command to create tables and set relationships in your database.

```bash
python3 manage.py migrate
```

or

```bash
django-admin migrate
```

Run
```bash
python3 manage.py runserver
```
And you are good to go

## Documentation

* Link to the [docs](https://documenter.getpostman.com/view/8822784/TzeZERwo)
* Link to the [collection](https://www.getpostman.com/collections/670f6ec08cabdf1a913b)

## Deployment link

https://develops-today-news.herokuapp.com/

## Linting & Formatting

Linting completed with flake8
```bash
flake8 --ignore E501 .
```

Formatting completed with black
```bash
black .
```