# Docker-django-nginx-postgres-gunicorn boilerplate
This repository you can for any python django rest project. just add new app.


Copy `.env.example` file to `.env`
-------------------------------------------
```bash
|
|--> example.env
|--> .env
```

Make a file name `.env.docker` add 
-----------------------------------------
```sh
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=blog
```

## Docker Up and Run

 - Docker Build
```sh
docker-compose up -d --build
```
- Let's Browse [http://0.0.0.0:8086](http://0.0.0.0:8086)
- Migration
```sh
docker-compose exec web python manage.py migrate --noinput
```
- Collect Statics 
```sh
docker-compose exec web python manage.py collectstatic --no-input --clear
```
- Check Logs
```sh
docker-compose logs -f
``` 
- Container down
```sh
docker-compose down
```

We have mounted database media and static file
-----------------------------------------
- Docker List Volume Mount
```sh
docker volume ls
```
- Docker Individual Volume
```sh
 docker inspect $name
```