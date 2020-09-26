# coinTracker

Cryptocoin tracker with redis



pip install requirements.txt

celery -A ccticker worker -l info
celery -A ccticker beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
