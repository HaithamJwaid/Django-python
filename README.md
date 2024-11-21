# Distributed-System

Create bookproject Python Django-Projekt

1- django-admin startproject bookproject

2- python3 manage.py startapp books

3- python3 manage.py makemigrations

4- python3 manage.py migrate

Superuser Create an admin user to manage the application:

5- python3 manage.py createsuperuser
# you can give also fake data like admin@admin.hj

Run Server Start the Django development server:

6- python3 manage.py runserver

Visit: http://127.0.0.1:8000/books/ for the book list
Visit: http://127.0.0.1:8000/admin/ for the admin interface


create a serialzer and Viewsets:

7- pip install djangorestframework

...
.
.
.
.
.
as comited

than call 
http://127.0.0.1:8000/

than

http://127.0.0.1:8000/api/

than

http://127.0.0.1:8000/api/books

than

http://127.0.0.1:8000/api/books/1/


