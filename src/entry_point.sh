#!/bin/bash
python manage.py makemigrations
python manage.py migrate
# until python manage.py migrate; do
#   sleep 2
#   echo "Retry!";
# done
python manage.py shell < init_admin.py

python manage.py makemigrations app
python manage.py migrate app
echo "Django is ready.";
python manage.py runserver 0.0.0.0:8000
