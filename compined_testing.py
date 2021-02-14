import requests
from db_connector import get_user
from selenium import webdriver

user_id = 1001
requests.post('http://localhost:5000/users/' + str(user_id), json={"user_name": "user name " + str(user_id)})
res = requests.get('http://localhost:5000/users/' + str(user_id))
assert res
assert get_user(str(user_id))[0][0] == "user name " + str(user_id)


driver = webdriver.Chrome(executable_path="/Users/basharegbariya/Downloads/chromedriver")
driver.get("http://127.0.0.1:5001/users/get_user_data/"+str(user_id))
assert driver.find_element_by_id("user").text == 'user name ' + str(user_id)
driver.quit()
