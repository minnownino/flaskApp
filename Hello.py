from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
#from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 5556
mysql.init_app(app)



@app.route('/')
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    # create user code will be here, we will use jQuery AJAX to post our signup data to the signUp method, so we specify the method in the route definition
    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    _hashed_password = generate_password_hash(_password)
    # validate the received values
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_createUser1',(_name,_email,_hashed_password))
    if _name and _email and _password:
        #return json.dumps({'html': '<span>All fields good !!</span>'})
        data = cursor.fetchall()
        if len(data) is 0:
            conn.commit()
            return json.dumps({'message':'User created successfully !'})
        else:
            return json.dumps({'error':str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    _hashed_password = generate_password_hash(_password)
    cursor = mysql.connect().cursor()
    #cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchall()
    if len(data) is 0:
        return json.dumps({'message':'User created successfully !'})
    else:
        return json.dumps({'error':str(data[0])})

if __name__ == '__main__':
    app.run()
