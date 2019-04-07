# redline-project
#### Car Modification Tracking Application

## Local development steps

* Clone repository locally
* Create your virtual environment
```
python3 -m venv /path/to/new/virtual/environment
```
* Start virtual environment
```
source /path/to/new/virtual/environment/bin/activate
```
* Configure your virtual environment with file included in repo
```
pip install -r requirements.txt
```
* Initialize db.sqlite3 database
```
python manage.py migrate
```
* Create database superuser
```
python manage.py createsuperuser
```

* Start server
```
python manage.py runserver
```

## Project Dependencies
#### Taken from requirements.txt

* certifi==2019.3.9
* chardet==3.0.4
* Django==2.1.7
* djangorestframework==3.9.1
* idna==2.8
* pkg-resources==0.0.0
* pycodestyle==2.5.0
* pytz==2018.9
* requests==2.21.0
* urllib3==1.24.1

## API Authenication
#### In order to make requests to API endpoints, you need an auth token

* Make a POST request to `POST '/api/v1/user/auth'` and include username and password key value pairs as JSON in the body of the request
* Place the auth token you receive in the header of each request
```
"Auhorization: Token [auth_token]"
```

## Frontend
#### There are currently four pages on the frontend
#### The frontend is fully static with no dynamic data as of now

* Dashboard - Home screen once logged in
* New Car - Page to add a new car to your account
* Login - Form to login
* Register - Form to register (Might combine this with login page)
* Car Detail - Shows specific information on a single car

* To see the frontend, start server
```
python manage.py runserver
```
* Navigate to 127.0.0.1:8000/
