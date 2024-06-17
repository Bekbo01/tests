web: gunicorn nameOfProject.wsgi --log-file -
worker: celery worker --app=myelearning --loglevel=info -B
release: python3 manage.py migrate
