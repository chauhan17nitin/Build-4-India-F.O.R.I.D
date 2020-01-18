import datetime
from flask import Flask, request, jsonify, flash
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
# Establishing connection to aws rds instance
import pymysql

connection = pymysql.connect(
#database-1.cxedn5oo3lwl.ap-south-1.rds.amazonaws.com
    host = 'database-1.cxedn5oo3lwl.ap-south-1.rds.amazonaws.com',
    port = int(3306),
    user = "admin",
    passwd = "admin123",
    db = 'agriculture',
    charset ='utf8mb4'
    )

@app.route('/', methods=['POST', 'GET'])
def index():
#    content = request.json
    content = request.json["hello"]
    world = request.json["time"]
    print(content)
    return world

##function for add user
@app.route('/add_user',methods=['POST', 'GET'])
def add_user():
    # cursor = mysql.connection.cursor()
	cursor = connection.cursor()
    # user_info = request.json['user_info']

	user_name = request.json['user_name']
	first_name = request.json['first_name']
	last_name = request.json['last_name']
	dob = request.json['dob']
	password = request.json['password']
	address = request.json['address']
	city = request.json['city']
	state = request.json['state']
#	query = "INSERT INTO user (user_name,first_name,last_name,dob,password,address,city,state) VALUES ( {}, {}, {}, '2038-01-19 03:14:07', {}, {}, {}, {})".format(user_name, first_name, last_name, password, address, str(city), state)
	query = "INSERT INTO user (user_name, first_name, last_name, dob, password, address, city, state) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
	values = [user_name, first_name, last_name, dob, password, address, city, state]
	try:
		cursor.execute(query, values)
		connection.commit()
		cursor.close()
		return jsonify({'code':200, 'message': 'user addition Successful'})
	except Exception as e:
    		cursor.close()
    		return jsonify({'code':400, 'message': str(e)})
# user login api
@app.route('/user_login', methods=['POST'])
def user_login():
    cursor = connection.cursor()
    user_name = request.json['user_name']
    password = request.json['password']

    query = "SELECT password from user where user_name = %s"
    values = [user_name]
    query_check = cursor.execute(query, values)
    password_db = cursor.fetchone()[0]
#    print(password_db[0])
    cursor.close()

    if password_db and password_db == password:
 #       flash("Login Successful")
        return jsonify({'code':200, 'message':'user login Successful'})
    else:
#        flash("Invalid credentials")
        return jsonify({'code':400, 'message': 'invalid credentials'})

# add field for user api
@app.route('/add_field', methods=['POST'])
def add_field():
    cursor = connection.cursor()
    user_name = request.json['user_name']
    field_name = request.json['field_name']
    length = request.json['length']
    width = request.json['width']

    query = "INSERT INTO fields (user_name,field_name,length,width) VALUES (%s, %s, %s, %s)"
    values = [user_name, field_name, length, width]

    try:
        cursor.execute(query, values)
        cursor.close()
        connection.commit()
        return jsonify({'code':200, 'message': 'field add success'})
    except Exception as e:
        cursor.close()
        return jsonify({'code':400, 'message': str(e)})

# delete field for user api usage yet to be decide ad deleting primary key will cause a lot of trouble
@app.route('/delete_field', methods=['POST'])
def delete_field():
    cursor = connection.cursor()
    user_name = request.json['user_name']
    field_name = request.json['field_name']

    query = "DELETE FROM fields WHERE user_name = %s and field_name = %s"
    values = [user_name, field_name]

    try:
        cursor.execute(query, values)
        cursor.close()
        connection.commit()
        return jsonify({'code': 200, 'message': 'field deletion success'})
    except Exception as e:
        cursor.close()
        return jsonify({'code': 400, 'message': str(e)})

# update field for user api
@app.route('/update_field', methods=['POST'])
def update_field():
    cursor = connection.cursor()
    field_id = request.json['field_id']
    field_name = request.json['field_name']
    length = request.json['length']
    width = request.json['width']

    query = "UPDATE fields SET field_name = %s, length = %s, width = %s WHERE field_id = %s"
    values = [field_name, length, width, field_id]

    try:
        cursor.execute(query, values)
        cursor.close()
        connection.commit()
        return jsonify({'code': 200, 'message': 'field updated Successfully'})
    except Exception as e:
        cursor.close()
        return jsonify({'code': 400, 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
