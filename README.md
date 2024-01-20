# <p align="center">Aiogram Mongo Template</p>

### <p align="center"><a href="https://core.telegram.org/bots/api">Telegram Bot</a> template with <a href="https://docs.aiogram.dev/en/dev-3.x/">aiogram</a>, <a href="https://www.mongodb.com/">mongodb</a> and <a href="https://www.docker.com/">docker</a></p>

## Technologies used:

- Aiogram
- Redis
- Motor
- MongoDB
- i18n
- Docker and docker compose

## Navigate

- [Getting started](#getting-started)
  - [Init project](#init-project)
  - [Configure environment variables](#configure-environment-variables)
    - [Bot config](#bot-config)
    - [Redis config](#redis-config)
    - [Database config](#database-config)
  - [Application start (local)](#application-start-local)
- [Docker](#docker)
  - [Application start (docker)](#application-start-docker)
  - [View app logs](#view-app-logs)
  - [Rebuild app](#rebuild-app)
  - [Manage mongodb](#manage-mongodb)

## Getting started

### Init project

```bash
$ git clone -b aiogram3 https://github.com/webshining/aiogram-mongo-template project_name
$ cd project_name
$ pip install -r requirements.txt
```

### Configure environment variables

> Copy variables from .env.ren file to .env

```bash
$ cp .env.ren .env
```

### Bot config

`TELEGRAM_BOT_TOKEN` - your bot token (required)

`I18N_DOMAIN` - locales file name

### Redis config

> If you are not using redis, by default used MemoryStorage

`RD_DB` - your redis database (number)

`RD_HOST` - your redis host

`RD_PORT` - your redis port

> You can specify RD_URI instead of RD_DB, RD_HOST and RD_PORT

`RD_URI` - connection url to your redis server

### Database config

> MongoDB URL format<br> > `mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]`

`MONGODB_URL` - connection url to your mongodb server

### Application start (local)

```bash
$ python main.py
# If you have make you can enter
$ make run
```

## Docker

### Application start (docker)

> Run only one service:<br> > `$ docker-compose up -d service-name`

```bash
$ docker-compose up -d
# If you have make you can enter
$ make rebuild
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
