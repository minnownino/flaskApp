from flask import Flask, render_template, request, json, url_for
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
#from flask_mysqldb import MySQL
from queries import *
from flask import jsonify
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

@app.route('/getgene/<sga>')
def getgene(sga):
    #jsonobject = [{"mut": 95, "cancertype": "BLCA", "del": 5, "amp": 0}, {"mut": 245, "cancertype": "BRCA", "del": 6, "amp": 0}, {"mut": 104, "cancertype": "COAD", "del": 2, "amp": 0}, {"mut": 129, "cancertype": "ESCA", "del": 2, "amp": 0}, {"mut": 66, "cancertype": "GBM", "del": 5, "amp": 0}, {"mut": 316, "cancertype": "HNSC", "del": 3, "amp": 1}, {"mut": 17, "cancertype": "KIRC", "del": 0, "amp": 0}, {"mut": 4, "cancertype": "KIRP", "del": 0, "amp": 0}, {"mut": 41, "cancertype": "LIHC", "del": 2, "amp": 0}, {"mut": 186, "cancertype": "LUAD", "del": 3, "amp": 0}, {"mut": 108, "cancertype": "LUSC", "del": 3, "amp": 0}, {"mut": 269, "cancertype": "OV", "del": 2, "amp": 4}, {"mut": 44, "cancertype": "PRAD", "del": 33, "amp": 0}, {"mut": 57, "cancertype": "READ", "del": 0, "amp": 0}, {"mut": 80, "cancertype": "STAD", "del": 3, "amp": 0}, {"mut": 41, "cancertype": "UCEC", "del": 0, "amp": 0}, {"mut": 1802, "cancertype": "all", "del": 3, "amp": 4}];
    data = allCTdistribution(sga)
    return jsonify(data)

@app.route('/gettopdegs/<sga>')
def getTopDEGs(sga):
    data = getTopDEGsPerCT(sga)
    return jsonify(data)

@app.route('/scatter/<sga>')
def getscatter(sga):
    return tumorInfo(sga)

@app.route('/stack/')
def stack():
    return render_template('stack_trial1.html')

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
