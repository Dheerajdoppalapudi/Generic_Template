# Generic_Template

This is a python based Flask Project. This project is intended to save time as the project contains basic authentication, authorization, audi loggin, error logging and unit testing. 

routes.py 
this file contains the endpoints like /login, /register /logout /about /home
  /resister - the user hits this route request when he wants to create a new account. this route takes the payload {"username": "", "email": "", "password: "", "conform_password": ""} the route also does the validation by checking if the user in alredy exsisting or not. upon sending the correct details via POST request, the route responds with the success api responce and a new row will be created in the table. 

  /login - this route take in {"username": "", "password": ""} upon correct details it will logs in the user with a success reaponce and session, if the user is already logged in then the api will respond with exisisting session. 

  /logout - this will logs out the current user

models.py
here is the file where in we stack out DB tables, for instance a User table is created for accounts

test
