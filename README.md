# Django with PostgreSQL

One-minute deployment, simple web-application.

*It is not recommended to deploy a core database as a container. This example shows how to handle the multi-container situation, when one container (Django) strongly depends on the other container (database).*


## Getting Started
![Screen Shopt](images/main-screenshot.png?raw=true "Screen Shot")
Two containers
  * web app(Django)
  * database(PostgreSQL)

If a container (Django) should be launched after another container(postgres) we can define it in the `depends_on` field.

```
version: '3.3'

services:
  app:
    build:
      context: ./src
      dockerfile: Dockerfile
    ports:
      - "8000:8000"
    depends_on:
      - db
  db:
    image: "postgres:13.5-alpine"
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

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

### Installation

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
