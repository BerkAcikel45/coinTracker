# coinTracker

Cryptocoin tracker with redis



pip install requirements.txt

celery -A coinTracker worker -l info
********
celery -A coinTracker beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
