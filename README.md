# tenner-api
Backend for Tenner

## Django Server
```
(venv) python manage.py runserver 0.0.0.0:8000
```

## Redis Server
```
(venv) redis-server --port 6380
```

## Celery Worker
```
(venv) celery -A api worker -l INFO
```

## Celery Beat
```
(venv) celery -A api beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
```
