# Generic_Template

This is a python based Flask Project. This project is intended to save time as the project contains basic authentication, authorization, audi loggin, error logging and unit testing. 

<h3>routes.py</h3>
This file contains the endpoints like /login, /register, /logout, /about, /home

 - /resister - the user hits this route request when he wants to create a new account. this route takes the payload {"username": "", "email": "", "password: "", "conform_password": ""} the route also does the validation by checking if the user in alredy exsisting or not. upon sending the correct details via POST request, the route responds with the success api responce and a new row will be created in the table. 

 - /login - this route take in {"username": "", "password": ""} upon correct details it will logs in the user with a success reaponce and session, if the user is already logged in then the api will respond with exisisting session. 

 - /logout - this will logs out the current user

<h3>models.py</h3>
Here is the file where in we stack out DB tables, for instance a User table is created for accounts

<h3>test/tests.py</h3>
This file is used for testing, creating test cases to validate the written code by different scenarios and edge cases.

<h3>__init__.py</h3>
This File contains the app configuration. as well as the logging this projects containg audit logging(audit_log.log file) and error loggin(logged in common_logs.log file)

<h3>run.py</h3>
This is thes entry point of the application we use python run.py to start the application in port:8000
