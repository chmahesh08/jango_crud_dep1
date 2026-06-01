python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn jango_crud_dep.wsgi:application --bind 0.0.0.0:$PORT