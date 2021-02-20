import requests

try:
    requests.get('http://127.0.0.1:5000/stop_server')
except:
    print("rest_app server are not responding")

try:
    requests.get('http://127.0.0.1:5001/stop_server')
except:
    print("wep_app server are not responding")
