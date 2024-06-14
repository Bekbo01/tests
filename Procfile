web: gunicorn nameOfProject.wsgi --log-file -
web: pip install -U pip setuptools
worker: celery worker --app=myelearning --loglevel=info -B
release: python3 manage.py migrate
