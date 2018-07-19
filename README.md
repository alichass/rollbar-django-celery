Installation:

* pip install -r requirements.txt
* Install redis server somehow (depends on your system)

Running:

In three different terminals, all in this working directory do:

* In terminal A: redis-server
* In terminal B: celery -A rbexample worker --loglevel=info
* In terminal C: python manage.py runserver
