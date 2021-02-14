from flask import Flask, request

from db_connector import get_user, post_user, update_user, delete_user

app = Flask(__name__)


# Rest api endpoint, accepts requests with 4 types
# ('GET', 'POST', 'DELETE', 'PUT') and user id and
# payload for some types
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    #
    # if request type was 'POST', the endpoint
    # will connect to db and add the user accepted
    # to the db, if the user exist it will return
    # proper message
    #
    if request.method == 'POST':
        request_data = request.json
        user_name = request_data.get('user_name')
        if post_user(user_name, user_id):
            return {'status': 'ok',
                    'user_added': user_name}, 200
        else:
            return {'status': 'error',
                    'reason': 'id already exist'}, 500
    #
    # if request type was 'GET', the endpoint
    # will call db to fetch data about user
    # will return data if exist, and will return
    # proper message if not
    #
    elif request.method == 'GET':
        result = get_user(user_id)
        if result:
            return {'status': 'ok',
                    'user_name': result}, 200
        else:
            return {'status': 'error',
                    'reason': 'no such id'}, 500
    # 'PUT' endpoint will update existing user
    # with new data, if user isn't exist, it will
    # return proper message
    elif request.method == 'PUT':
        request_data = request.json
        user_name = request_data.get('user_name')
        if get_user(user_id):
            update_user(user_name, user_id)
            return {'status': 'ok',
                    'user_updated': user_name}, 200
        else:
            return {'status': 'error',
                    'reason': 'no such id'}, 500
    # 'DELETE' endpoint will delete user if exist
    # and will return proper message if not
    elif request.method == 'DELETE':
        if get_user(user_id):
            delete_user(user_id)
            return {'status': 'ok',
                    'user_deleted': user_id}, 200
        else:
            return {'status': 'error',
                    'reason': 'no such id'}, 500


app.run(host='127.0.0.1', debug=True, port=5000)
