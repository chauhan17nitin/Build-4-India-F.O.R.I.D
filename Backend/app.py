
import datetime
from flask import Flask, request, jsonify, flash
from flask_cors import CORS
app = Flask(__name__)
import json
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
 #   content = request.json["hello"]
 #   world = request.json["time"]
  #  print(content)
    return "world"


# check username presence
@app.route('/check_username', methods=['POST'])
def check_username():
    cursor = connection.cursor()
    user_name = request.json['user_name']

    values = [user_name]

    query = "SELECT user_name FROM user WHERE user_name = %s"

    query_check = cursor.execute(query, values)
    output = cursor.fetchall()

    if output:
        cursor.close()
        return "{'message' : 'username not available'}"
    else:
        cursor.close()
        return "{'message' :'user name available'}"

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
	mobile = request.json['mobile']
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
		
		return str({'code':200, 'message': 'user addition Successful'})
	except Exception as e:
		
    		cursor.close()
		
    		return str({'code':400, 'message': 'exception occured'})


# user login api
@app.route('/user_login', methods=['POST', 'GET'])
def user_login():
    cursor = connection.cursor()
    user_name = request.json['user_name']
    password = request.json['password']

    query = "SELECT password from user where user_name = %s"
    values = [user_name]
    query_check = cursor.execute(query, values)
    password_db = cursor.fetchone()
#    print(password_db[0])

    if password_db and password_db[0] == password:
 #       flash("Login Successful")
        query2 = "SELECT first_name from user where user_name = %s"
        query2_check = cursor.execute(query2, values)
        first_name = str(cursor.fetchone()[0])
        cursor.close()
        message = "{'message': 'user login succesful', 'first_name': '" + first_name + "' }"
        return (message)
#        return ('{"code":200, "message":"user login Successful", "first_name": {} }').format(first_name)
    else:
#        flash("Invalid credentials")
        cursor.close()
        return str({'code':400, 'message': 'invalid credentials'})

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
        return str({'code':200, 'message': 'field add success'})
    except Exception as e:
        cursor.close()
        return str({'code':400, 'message': str(e)})

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

# add crops by admin of maintainer or may be user yet to decide
@app.route('/add_crop', methods=['POST'])
def add_crop():
    cursor = connection.cursor()
    crop_name = request.json['crop_name']
    seasonality = request.json['seasonality']
    crop_wiki = request.json['crop_wiki']
    query = "INSERT INTO crops (crop_name, seasonality, crop_wiki) VALUES (%s, %s, %s)"
    values = [str(crop_name), str(seasonality), crop_wiki]
    print(values)
    try:
        cursor.execute(query, values)
        cursor.close()
        connection.commit()
        return jsonify({'code': 200, 'message': 'crop added Successfully'})
    except Exception as e:
        cursor.close()
        return jsonify({'code': 400, 'message': str(e)})

# update crops privileges yet to be decide
@app.route('/update_crop', methods=['POST'])
def update_crop():
    cursor = connection.cursor()
    crop_id = request.json['crop_id']
    crop_name = request.json['crop_name']
    seasonality = request.json['seasonality']
    crop_wiki = request.json['crop_wiki']
    query = "UPDATE crops SET crop_name = %s, seasonality = %s, crop_wiki = %s WHERE crop_id = %s"
    values = [crop_name, seasonality, crop_wiki, crop_id]

    try:
        cursor.execute(query, values)
        cursor.close()
        connection.commit()
        return jsonify({'code': 200, 'message': 'crop updated Successfully'})
    except Exception as e:
        cursor.close()
        return jsonify({'code': 400, 'message': str(e)})

@app.route('/add_crop_history', methods=['POST'])
def add_crop_history():
    cursor = connection.cursor()
    user_name = request.json['user_name']
    field_id = request.json['field_id']
    sowing_time = request.json['sowing_time']
    crop_id = request.json['crop_id']

    query = "INSERT INTO crop_history (user_name, field_id, sowing_time, crop_id) VALUES (%s, %s, %s, %s)"

    values = [user_name, field_id, sowing_time, crop_id]

    try:
        cursor.execute(query, values)
        cursor.close()
        connection.commit()
        return jsonify({'code': 200, 'message': 'crop history added Successfully'})
    except Exception as e:
        cursor.close()
        return jsonify({'code': 400, 'message': str(e)})


# updating crop history by user
@app.route('/update_crop_history', methods=['POST'])
def update_crop_history():
    cursor = connection.cursor()
    field_id = request.json['field_id']
    sowing_time = request.json['sowing_time']
    harvesting_time = request.json['harvesting_time']
    total_yield = request.json['total_yield']
    amount_sold = request.json['amount_sold']

    query = "UPDATE crop_history SET harvesting_time = %s, total_yield = %s, amount_sold = %s WHERE field_id = %s and sowing_time = %s"    
    
    values = [harvesting_time, total_yield, amount_sold, field_id, sowing_time]

    try:
        cursor.execute(query, values)
        cursor.close()
        connection.commit()
        return jsonify({'code': 200, 'message': 'crop in the field updated'})
    except Exception as e:
        connection.rollback()
        cursor.close()
        return jsonify({'code': 400, 'message': str(e)})


# select crop for user
@app.route('/select_crop', methods=['POST'])
def select_crop():
    cursor = connection.cursor()
    query = "SELECT JSON_ARRAYAGG(JSON_OBJECT('crop_name', crop_name, 'seasonality', seasonality)) FROM crops"

    try:
        query_check = cursor.execute(query)
        output = cursor.fetchall()
        #print(type(output[0][0]))
        #json_output = json.dumps(output)
        cursor.close()
        connection.commit()
        return output[0][0]
    except Exception as e:
        cursor.close()
        return jsonify({'code': 400, 'message': str(e)})


# history update api after scanning
@app.route('/scan_update', methods=['POST'])
def scan_update():
    cursor = connection.cursor()
    user_name = request.json['user_name']
    field_id = request.json['field_id']
    scan_time = request.json['scan_time']
    percent_damage = request.json['percent_damage']
    file_path = request.json['file_path']
    spray_status = request.json['spray_status']
    crop_id = request.json['crop_id']

    query = "INSERT INTO scan_history (user_name, field_id, scan_time, percent_damage, file_path, spray_status, crop_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"

    values = [user_name, field_id, scan_time, percent_damage, file_path, spray_status, crop_id]

    try:
        cursor.execute(query, values)
        cursor.close()
        connection.commit()
        return jsonify({'code': 200, 'message': 'scan updated Successfully'})
    except Exception as e:
        cursor.close()
        return jsonify({'code': 200, 'message': str(e)})


# view scan history for particular user
@app.route('/scan_history_user', methods=['POST'])
def scan_history_user():
    cursor = connection.cursor()
    user_name = request.json['user_name']

    query = "SELECT JSON_ARRAYAGG(JSON_OBJECT('field_name', fields.field_name, 'scan_time', scan_history.scan_time, 'percent_damage', scan_history.percent_damage, 'crop_name', crops.crop_name)) from scan_history, crops, fields WHERE scan_history.user_name = %s and crops.crop_id = scan_history.crop_id and fields.field_id = scan_history.field_id ORDER BY scan_time DESC"


    values = [user_name]

    try:
        query_check = cursor.execute(query, values)
        output = cursor.fetchall()

        cursor.close()
        connection.commit()
        return output[0][0]
    except Exception as e:
        cursor.close()
        return jsonify({'code': 400, 'message': str(e)})


# view available fields for user
@app.route('/field_for_user', methods=['POST'])
def field_for_user():
    cursor = connection.cursor()
    user_name = request.json['user_name']

    query = "SELECT JSON_ARRAYAGG(JSON_OBJECT('field_name', field_name, 'field_id', field_id)) FROM fields WHERE user_name = %s"
    values = [user_name]

    try:
        query_check = cursor.execute(query, values)
        output = cursor.fetchall()
        cursor.close()

        connection.commit()
        return output[0][0]
    except Exception as e:
        cursor.close()
        return jsonify({'code': 400, 'message': str(e)})

# finding information of particular field
@app.route('/field_information2', methods=['POST'])
def field_information2():
    cursor = connection.cursor()

    field_id = request.json['field_id']

    query = "SELECT JSON_ARRAYAGG(JSON_OBJECT('length', fields.length, 'width', fields.width, 'crop_name', crops.crop_name, 'sowing_time', crop_history.sowing_time)) OVER(ORDER BY crop_history.sowing_time DESC) FROM fields, crop_history, crops WHERE crop_history.field_id = %s and fields.field_id = %s and crop_history.crop_id = crops.crop_id"

    # query_check = "SELECT fields.field_name, crops.crop_name FROM fields, crop_history, crops WHERE crop_history.field_id = fields.field_id = %s and crop_history.crop_id = crops.crops "

    values = [field_id, field_id]

    try:
        query_check = cursor.execute(query, values)
        output = cursor.fetchall()
        print(output)
        cursor.close()
        return output[0][0]
    except Exception as e:
        cursor.close()

        return jsonify({'code': 400, 'message': str(e)})

# finding information of particular field
@app.route('/field_information', methods=['POST'])
def field_information():
    cursor = connection.cursor()

    field_id = request.json['field_id']

    values = [field_id]
    values2 = [field_id, field_id]
    query1 = "SELECT user_name FROM crop_history WHERE field_id = %s"

    try:
        query_check = cursor.execute(query1, values)
        output = cursor.fetchone()
    except Exception as e:
        return jsonify({'code': 400, 'message': str(e)})
    print(output)
    if output:
        query = "SELECT JSON_ARRAYAGG(JSON_OBJECT('length', fields.length, 'width', fields.width, 'crop_name', crops.crop_name, 'sowing_time', crop_history.sowing_time)) OVER(ORDER BY crop_history.sowing_time DESC)FROM fields, crop_history, crops WHERE crop_history.field_id = %s and fields.field_id = %s and crop_history.crop_id = crops.crop_id"
        try:
            query_check = cursor.execute(query, values2)
            output = cursor.fetchall()
            cursor.close()

            return output[0][0]
        except Exception as e:
            cursor.close()

            return jsonify({'code': 400, 'message': str(e)})                 
    else:
        query2 = "SELECT JSON_ARRAYAGG(JSON_OBJECT('length', fields.length, 'width', fields.width)) FROM fields WHERE fields.field_id = %s"
        
        try:
            query_check = cursor.execute(query2, values)
            output = cursor.fetchall()
            cursor.close()
            return output[0][0]
        except Exception as e:
            cursor.close()
            return jsonify({'code': 400, 'message': str(e)})



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
