# SSBW
Prácticas de la asignatura Sistemas Software Basados en Web

```
source bin/activate
cd Restaurantes
python manage.py runserver

python manage.py syncdb --no-initial-data
python manage.py makemigrations
python manage.py migrate

python populate.py
```
