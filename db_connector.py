import datetime
import psycopg2


# Post Method to get as variables, user name and
# user id as input
# and Insert them into users table
# Returns true if Insertion succeeded, false if not

def post_user(user_name, user_id):
    con = psycopg2.connect(database="db", user="docker_user", password="password", host="database", port=5432)
    cur = con.cursor()
    current_date_time = datetime.datetime.now()
    sql = "INSERT into USERS (user_name, user_id, creation_date) VALUES " \
          "('" + user_name + "'," + user_id + ",'" + str(current_date_time) + "')"

    # using prepared statements (Extras sec.2)
    stmt = "INSERT into USERS (user_name, user_id, creation_date) VALUES (%s,%s,%s)"
    insert_tuple = (user_name, user_id, str(current_date_time))
    try:
        # cur.execute(sql)
        cur.execute(stmt, insert_tuple)
        con.commit()
        return True
    except:
        return False
    finally:
        cur.close()
        con.close()


# Get Method to get as variable, user id as input
# and return user name if exist and empty string if not
# @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_delay=30000)
def get_user(user_id):
    con = psycopg2.connect(database="db", user="docker_user", password="password", host="database", port=5432)
    cur = con.cursor()
    sql = "SELECT user_name FROM USERS WHERE user_id=" + user_id + ";"
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
    con = psycopg2.connect(database="db", user="docker_user", password="password", host="database", port=5432)
    cur = con.cursor()
    sql = "UPDATE USERS SET user_name = '" + user_name + "' WHERE user_id = " + user_id + ";"
    try:
        cur.execute(sql)
        con.commit()
        return cur.fetchall()
    except:
        return False
    finally:
        cur.close()
        con.close()


# Delete Method to accept user id as input
# and deletes the user from db if exist
def delete_user(user_id):
    con = psycopg2.connect(database="db", user="docker_user", password="password", host="database", port=5432)
    cur = con.cursor()
    sql = "DELETE FROM USERS WHERE user_id =" + user_id + ";"
    try:
        cur.execute(sql)
        con.commit()
        return cur.fetchall()
    except:
        return False
    finally:
        cur.close()
        con.close()
