import os
import signal

from flask import Flask
from db_connector import get_user

app = Flask(__name__)


# web interface endpoint that will use flask to
# present response returned from get_user_name method,
# the responses will be html that will contain the user
# if user exist and a proper message if not, method will
# call get_user method that fetch data from db
@app.route('/users/get_user_data/<user_id>')
def get_user_name(user_id):
    user_name = get_user(user_id)
    if user_name:
        user_name_str = str(user_name[0][0])
        return "<H1 id='user'>" + user_name_str + "</H1>"
    else:
        return "<H1 id='error'> no such user:" + user_id + "</H1>"


app.run(host='127.0.0.1', debug=True, port=5001)


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'
