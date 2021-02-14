from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/basharegbariya/Downloads/chromedriver")
driver.get("http://127.0.0.1:5001/users/get_user_data/9")
assert driver.find_element_by_id("user").text == 'new user'
driver.quit()
