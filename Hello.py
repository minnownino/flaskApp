from flask import Flask, render_template, request, json, url_for
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
#from flask_mysqldb import MySQL
from queries import *

app = Flask(__name__)
mysql = MySQL(app)
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'TDI'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

@app.route('/test/')
def test():
    name = request.form['SGA']
    #return render_template('test.html', name = name)
    return render_template('test.html', name = name)
    
@app.route('/')
def main():
    (all_distribution, driver_distribution, cancer_types) = getSGACTdistribution('MUC6')
    all_distribution = list(int(i[1]) for i in all_distribution)
    driver_distribution = list(int(i[1]) for i in driver_distribution)
    return render_template('index.html', all_distribution = all_distribution, driver_distribution = driver_distribution, cancer_types = cancer_types)
    
    #return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/test/', methods=['POST', 'GET'])
def result():
    name = str(request.form.get('SGA', None))
    (all_distribution, driver_distribution, cancer_types) = getSGACTdistribution(name)
    all_distribution = list(int(i[1]) for i in all_distribution)
    driver_distribution = list(int(i[1]) for i in driver_distribution)
    return render_template('result.html', all_distribution = all_distribution, driver_distribution = driver_distribution, cancer_types = cancer_types)
    #return render_template('result.html', name = name)
if __name__ == '__main__':
    app.run()