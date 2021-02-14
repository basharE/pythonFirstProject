import requests
from db_connector import get_user

user_id = 1000
requests.post('http://localhost:5000/users/' + str(user_id), json={"user_name": "user name " + str(user_id)})
res = requests.get('http://localhost:5000/users/' + str(user_id))
assert res
assert get_user(str(user_id))[0][0] == "user name " + str(user_id)
