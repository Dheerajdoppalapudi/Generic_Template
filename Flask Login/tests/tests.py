import requests

def test_get_list_of_users():
    url = "http://127.0.0.1:8000/home"
    response = requests.get(url)
    assert response.status_code == 200 

def test_create_new_user():
    url = "http://127.0.0.1:8000/register"
    data = {
        "username": "state streetsdfbgfd",
        "email": "ss@gmail.comsdfggv",
        "password": "ss",
        "confirm_password": "ss"
    }
    response = requests.post(url, data=data)
    assert response.status_code == 201