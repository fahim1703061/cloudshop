# cloudshop

An e-commerce website

django --version 3.2.2

virtual env: venv

database -- mysql

note for mysql: python version 3.6.5 mysqlclient 1.4.0, other version may not work

venv\Scripts\activate
py manage.py check

py manage.py makemigrations
py manage.py migrate

py manage.py runserver

rulls to shift from one db to another

1. python manage.py dumpdata > db.json
2. Change the database settings to new database such as of MySQL / PostgreSQL.
3. python manage.py migrate
4. python manage.py shell
5. Enter the following in the shell
6. --from django.contrib.contenttypes.models import ContentType
7. --ContentType.objects.all().delete()
8. python manage.py loaddata db.json
