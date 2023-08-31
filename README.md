# Generic_Template

The project is based on the Flask framework, a Python-based framework. The purpose of the project is to simplify the process of logging in and out of an application by incorporating basic authentication, authorization, audit logging and error logging into the same application. 

<h3>routes.py</h3>
This file contains the endpoints like /login, /register, /logout, /about, /home

 - /resister - In order to create a new account, the user hits this route request. The route checks to see if the user already exists by taking {"username":"", "email":"", "password": "", and "conform_password": ""} as the payload. When the route receives the correct details via POST request, it returns the success API response and creates a new row in the table.

 - /login - The route takes {"username": "", "password": ""} upon correct details, it will log in the user with a success response and session, if the user is already logged in, the API will respond with the existing session. 

 - /logout - this will logs out the current user

<h3>models.py</h3>
Here is the file where in we stack out DB tables, for instance a User table is created for accounts

<h3>test/tests.py</h3>
This file is used for testing, creating test cases to validate the written code by different scenarios and edge cases.

<h3>__init__.py</h3>
The configuration of the app can be found in this file. Additionally, this project includes audit logging (audit_log.log file) and error logging (common_logs.log file).

<h3>run.py</h3>
Here is the entry point of the application, we use python run.py to start it on port 8000.

## Steps to run the Application

1. Clone the repository
2. Create a virtual environment
```
$ python -m venv env
```
3. Activate the virtual environment
```
> py env\Scripts\activate
```
4. Install the requirements
   navigate to folder which has requirements.txt
```
pip install -r requirements.txt
```
5. Navigate to folder which contains the run.py file
```
py run.py
```


------------------------
How to run the Tests
------------------------
Go the the folder tests/tests.py

use command 
```
pytest tests.py
```
