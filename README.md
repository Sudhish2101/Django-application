# Django-application
This is a django based application that builds an API to serve the data in the JSON format. 

**manage.py file**: CLI of the project for interacting with it.
**models.py file**: Defines the schema of the database
**serializers.py file**: Used to convert the data sent in a http request to a valid response data.

## Commands
**python manage.py runserver**: For starting the development server.
**python manage.py migrate**: To create tables in the database (by default SQLite) at the start and whenever any change is made in the models file.
