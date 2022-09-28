# <p align="center">Aiogram Mongo Template</p>

## Technologies used:
* Aiogram
* Redis
* Pymongo
* MongoDB
* Poetry
* Docker and docker compose

## Navigate
* [Getting started](#getting-started)
    * [Init project](#init-project)
    * [Configure environment variables](#configure-environment-variables)
        * [Bot config](#bot-config)
        * [Redis config](#redis-config)
        * [Database config](#database-config)
    * [Application start (local)](#local-start)
* [Docker](#docker)
    * [Application start (docker)](#docker-start)
## Getting started
### Init project
```bash
$ git clone https://github.com/webshining/aiogram-mongo-template project_name
$ cd project_name
$ pip install -r requirements.txt
$ poetry install # If you use poetry. Don't forget to select an interpreter
```
### Configure environment variables
> Copy variables from .env.ren file to .env
```bash
$ cp .env.ren .env
```
### Bot config
`TELEGRAM_BOT_TOKEN` - your bot token (required)

`ADMINS` - admin ids (not required)

### Redis config
> If you are not using redis, by default used MemoryStorage

`RD_DB` = redis database (number)

`RD_HOST` = redis host

`RD_PORT` = redis port

`RD_PASS` = redis password (not required)
### Database config
`MONGODB_URL` - connection url to your mongodb server
> MongoDB URL format`mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]`

### Application start (local)
```bash
$ python app.py 
```