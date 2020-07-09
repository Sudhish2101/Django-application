# Django-application
This is a django based application that builds an API to serve the data in the JSON format. 

## Files
* **manage.py file**: CLI of the project for interacting with it.   
* **models.py file**: Defines the schema of the database.  
* **serializers.py file**: Used to convert the data sent in a http request to a valid response data.  
* **gen_random.py**: Python script for generating random data and posting it on the deployed URL.

## Commands
* **python manage.py runserver**: For starting the development server.  
* **python manage.py migrate**: To create tables in the database (by default SQLite) at the start and whenever any change is made in the models file.  
* **python gen_random.py**: Populates the database with dummy data

 **Deployed URL** : "http://35.241.91.76:8000/api/myapp/"
