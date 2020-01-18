import datetime
from flask import Flask, request, jsonify, flash
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
# Establishing connection to aws rds instance
import pymysql

connection = pymysql.connect(
    host = 'database-1.cxedn5oo3lwl.ap-south-1.rds.amazonaws.com',
    port = int(3306),
    user = "admin",
    passwd = "admin123",
    db = 'agriculture',
    charset ='utf8mb4'
    )

@app.route('/')
def index():
    return_statement = "Hello World"
    return return_statement

##function for add user
@app.route('/add_user',methods=['POST'])
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

    query = "INSERT INTO user (user_name,first_name,last_name,dob,password,address,city,state) VALUES ( user_name, first_name, last_name, dob, password, address, city, state)"
	try:
		cursor.execute(query) 
		cursor.close()   
		connection.commit()
		return jsonify({'code':200, 'message': 'user addition Successful'})
	except Exception as e:
    	cursor.close()
    	return jsonify({'code':400, 'message': 'user addition Successful'})
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)