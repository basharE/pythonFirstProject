import pymysql
import datetime


# Post Method to get as variables, user name and
# user id as input
# and Insert them into users table
# Returns true if Insertion succeeded, false if not
def post_user(user_name, user_id):
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='main_schema')
    con.autocommit(True)
    cur = con.cursor()
    current_date_time = datetime.datetime.now()
    sql = "INSERT into main_schema.USERS (user_name, user_id, creation_date) VALUES " \
          "('" + user_name + "'," + user_id + ",'" + str(current_date_time) + "')"

    # using prepared statements (Extras sec.2)
    stmt = "INSERT into main_schema.USERS (user_name, user_id, creation_date) VALUES (%s,%s,%s)"
    insert_tuple = (user_name, user_id, str(current_date_time))
    try:
        # cur.execute(sql)
        cur.execute(stmt, insert_tuple)
        return True
    except:
        return False
    finally:
        cur.close()
        con.close()


# Get Method to get as variable, user id as input
# and return user name if exist and empty string if not
def get_user(user_id):
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='main_schema')
    cur = con.cursor()
    sql = "SELECT user_name FROM main_schema.USERS WHERE user_id=" + user_id
    try:
        cur.execute(sql)
        return cur.fetchall()
    except:
        return False
    finally:
        cur.close()
        con.close()


# Update Method accept user name and user id
# as input, and update the user name for
# specific id if exist by the new user name
def update_user(user_name, user_id):
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='main_schema')
    con.autocommit(True)
    cur = con.cursor()
    sql = "UPDATE main_schema.USERS SET user_name = '" + user_name + "' WHERE user_id = " + user_id
    try:
        cur.execute(sql)
        return cur.fetchall()
    except:
        return False
    finally:
        cur.close()
        con.close()


# Delete Method to accept user id as input
# and deletes the user from db if exist
def delete_user(user_id):
    con = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='12345678', db='main_schema')
    con.autocommit(True)
    cur = con.cursor()
    sql = "DELETE FROM main_schema.USERS WHERE user_id =" + user_id
    try:
        cur.execute(sql)
        return cur.fetchall()
    except:
        return False
    finally:
        cur.close()
        con.close()
