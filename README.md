# Tenner API

Backend for Tenner, the music-focused social media platform.

NOT YET DEPLOYED.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

See what the world is listening to with Tenner, the music-focused social media platform.

## Features

### Shared Listening Activity

View your friends' and favorite artists, athcetes, and celebrities' listening activity live.

### Multi-Platform

Bridge the gap between the major music streaming services by viewing a user's listening activity no matter which service they use!

WIP. Currently supports Spotify.

## Usage

### Django Server
```
(venv) python manage.py runserver 0.0.0.0:8000
```

### Redis Server
```
(venv) redis-server --port 6380
```

### Celery Worker
```
(venv) celery -A api worker -l INFO
```

### Celery Beat
```
(venv) celery -A api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

## License

MIT License.

## Acknowledgments

Utilizes the [Spotify API](https://developer.spotify.com/documentation/web-api).
