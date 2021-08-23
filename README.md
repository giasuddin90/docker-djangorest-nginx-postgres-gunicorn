# Docker-django-nginx-postgres-gunicorn boilerplate
This repository you can for any python django rest project. just add new app. We create this project by using
django rest, postgresql, nginx and gunicorn

If you love this project give me a star,that will motivate me to create more.
-------------------------------------------


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

Change your expected domain in nginx.conf file
-----------------------------------------
[Change Nginx Conf](nginx/nginx.conf)
```sh
 server_name www.example.com
 proxy_set_header Host www.example.com;
```


## Docker Up and Run

 - Docker Build
```sh
docker-compose up -d --build
```
- Let's Browse [http://0.0.0.0:8086](http://0.0.0.0:8086)
- Migration and super user create
```sh
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py createsuperuser
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