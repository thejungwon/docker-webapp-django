# Pizza ordering system
Forked from: https://github.com/thejungwon/docker-webapp-django

## Prerequists
- Clone this directory
- Install docker for any desktop platforms (Linux, Windows, MacOS)
- Open a shell in the cloned direcetory (the folder called pizza-ordering-system)
- Run './encode_data.sh' script. You can enter anything here but email sending needs valid gmail account's username and password (see [feature/12](https://github.com/fovecsernyes/pizza-ordering-system/tree/feature/12)).
- Type in './build_images.sh' and wait until the Docker images are ready (only neccessary for the first time and after changes in the Dockerfile)
- Type in './run_app.sh' and wait until everything is up
- The website should be reachable from any browsers at localhost:8000

## Important
- Please do not forget that Python usees **snake_case**!
- Use a plugin in your IDE that understands `.editorconfig`
- Apply formatting rules often!

## Built With

* [Django](https://www.djangoproject.com/) - Web framework
* [PostgreSQL](https://www.postgresql.org/) - Database
* [Unsplash](https://source.unsplash.com/) - External API
* [Bootstrap](https://getbootstrap.com/) - Front-end framework

