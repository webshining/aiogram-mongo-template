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
    * [Application start (local)](#application-start-local)
* [Docker](#docker)
    * [Application start (docker)](#application-start-docker)
    * [View app logs](#view-app-logs)
    * [Rebuild app](#rebuild-app)
    * [Manage mongodb](#manage-mongodb)
## Getting started
---
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
> MongoDB URL format<br>
`mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]`

`MONGODB_URL` - connection url to your mongodb server

### Application start (local)
```bash
$ python app.py 
# If you have make you can enter
$ make run
```
## Docker
---
### Application start (docker)
> Run only one service:<br>
`$ docker-compose up -d service-name`
```bash
$ docker-compose up -d
# If you have make you can enter
$ make compose
```
### View app logs
```bash
$ docker-compose logs -f app 
# If you have make you can enter
$ make logs
```
### Rebuild app
```bash
$ docker-compose up -d --build --no-deps --force-recreate
# If you have make you can enter
$ make rebuild
```
### Manage mongodb
```bash
$ docker-compose exec mongo mongosh
# If you have make you can enter
$ make mongosh
```