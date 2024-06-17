# web: gunicorn nameOfProject.wsgi --log-file -
web: python manage.py runserver
worker: celery worker --app=myelearning --loglevel=info -B
release: python3 manage.py migrate
