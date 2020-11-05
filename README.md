# Radix Django with PostgreSQL

One-minute deployment, simple web-application.

*It is not recommended to deploy a database to the instance. This example shows how to handle the multi-container situation, especially when one container(Django) strongly depends on the other container(database).*


## Getting Started
![Screen Shopt](images/main-screenshot.png?raw=true "Screen Shot")
Two containers
  * web app(Django)
  * database(PostgreSQL)

When we launch the application with a `docker-composer,` it is impossible to predict the finishing time.
This can be a big problem when one container has to be launched while the other container is properly running.

In this example, PostgreSQL needs more time to be launched than the Django application when it is its first launch. However, the Django application needs to be connected with a database before it starts to run.

In the dockerfile, we should run the container with some additional tactics like in `entry_point.sh`.

```
#!/bin/bash
cd src
python manage.py makemigrations

#until it succeeds
until python manage.py migrate; do
  sleep 2
  echo "Retry!";
done

python manage.py shell < init_admin.py
python manage.py makemigrations app
python manage.py migrate app
echo "Django is ready.";
python manage.py runserver 0.0.0.0:8000
```




### Prerequisites

Make sure you have already installed both Docker Engine and Docker Compose.
You don’t need to install Python or PostgreSQL, as both are provided by Docker images.

```
$ docker -v
Docker version 18.03.1-ce, build 9ee9f40
$ docker-compose -v
docker-compose version 1.21.1, build 5a3f1a3
```

### Installing

```
git clone https://github.com/thejungwon/docker-webapp-django.git
cd docker-webapp-django
docker-compose up
```

## Running the tests

TBD

### Break down into end to end tests

TBD

### And coding style tests

TBD



## Built With

* [Django](https://www.djangoproject.com/) - Web framework
* [PostgreSQL](https://www.postgresql.org/) - Database
* [Unsplash](https://source.unsplash.com/) - External API
* [Bootstrap](https://getbootstrap.com/) - Front-end framework


## Authors

* **Jungwon Seo** - *Initial work* - [thejungwon](https://github.com/thejungwon)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
