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
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''
app.config['MYSQL_DATABASE_PORT'] = 
mysql.init_app(app)


@app.route('/search/')
def search():
    return render_template('search.html')



@app.route('/layout/', methods=['POST', 'GET'])
def test():
    SGA = request.form['SGA']
    
    # prepare data for SM plot
    (SM_results, CN_AMP_results, CN_DEL_results) = getdriverAlterCTdistribution(SGA)
    #modify the results for plot
    SM_data = [0] * 16
    for result in SM_results:
        SM_data[result[0] - 1] = int(result[1])
    CN_AMP_data = [0] * 16
    for result in CN_AMP_results:
        CN_AMP_data[result[0] - 1] = int(result[1])
    CN_DEL_data = [0] * 16
    for result in CN_DEL_results:
        CN_DEL_data[result[0] - 1] = int(result[1])

    # prepare data for driver/SGA plot
    (all_distribution, driver_distribution, cancer_types) = getSGACTdistribution(SGA)
    all_distribution = list(int(i[1]) for i in all_distribution)
    driver_distribution = list(int(i[1]) for i in driver_distribution)

    # prepare data for deg table
    CT = {1:"BLCA", 2:"BRCA", 3:"COAD", 4:"ESCA", 5:"GBM", 6:"HNSC", 7:"KIRC", 8:"KIRP", 9:"LIHC", 10:"LUAD", 11:"LUSC", 12:"OV", 13:"PRAD", 14:"READ", 15:"STAD", 16:"UCEC"}
    Cancer_types = CT.values()
    (data_CTdistribution, deglist) = getDEGlistAndCTdistribution(SGA)
    data = {}
    data["data"] = []
    for deg in deglist:
        component = []
        component.append(deg[0])
        component.append(str(int(deg[1])))
        data["data"].append(component)
    
    return render_template('result_all.html', all_distribution = all_distribution, driver_distribution = driver_distribution, cancer_types = cancer_types)
    
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

@app.route('/alter/', methods=['POST', 'GET'])
def alter():
    SGA = request.form['SGA']
    (SM_results, CN_AMP_results, CN_DEL_results) = getdriverAlterCTdistribution(SGA)
    #modify the results for plot
    SM_data = [0] * 16
    for result in SM_results:
        SM_data[result[0] - 1] = int(result[1])
    CN_AMP_data = [0] * 16
    for result in CN_AMP_results:
        CN_AMP_data[result[0] - 1] = int(result[1])
    CN_DEL_data = [0] * 16
    for result in CN_DEL_results:
        CN_DEL_data[result[0] - 1] = int(result[1])
    return render_template('alter.html', SM_data = SM_data, CN_AMP_data = CN_AMP_data, CN_DEL_data = CN_DEL_data)


@app.route('/test/', methods=['POST', 'GET'])
def result():
    name = str(request.form.get('SGA', None))
    (all_distribution, driver_distribution, cancer_types) = getSGACTdistribution(name)
    all_distribution = list(int(i[1]) for i in all_distribution)
    driver_distribution = list(int(i[1]) for i in driver_distribution)
    return render_template('result.html', all_distribution = all_distribution, driver_distribution = driver_distribution, cancer_types = cancer_types)
    #return render_template('result.html', name = name)

@app.route('/tabledata/', methods = ['POST', 'GET'])
def tabledata():
    CT = {1:"BLCA", 2:"BRCA", 3:"COAD", 4:"ESCA", 5:"GBM", 6:"HNSC", 7:"KIRC", 8:"KIRP", 9:"LIHC", 10:"LUAD", 11:"LUSC", 12:"OV", 13:"PRAD", 14:"READ", 15:"STAD", 16:"UCEC"}
    Cancer_types = CT.values()
    SGA = request.args.get('SGA')
    #SGA = str(request.form['SGA'])
    #SGA = 'TP53'
    (data_CTdistribution, deglist) = getDEGlistAndCTdistribution(SGA)
    data = {}
    data["data"] = []
    for deg in deglist:
#        component = dict((item, 0) for item in Cancer_types)
        component = []
        component.append(deg[0])
        component.append(str(int(deg[1])))
#        component["DEG"] = deg[0]
#        component["Total"] = int(deg[1])
#         query = "select P.cancer_type_id, count(*) from SigSGADEGTumor as S, Patients as P where S.driver_gene_name = '%s' and S.DEG_name = '%s' and S.tumor_name = P.name group by P.cancer_type_id"%('TP53', deg[0])
#         cursor.execute(query)
#         results = cursor.fetchall()
#         for item in row:
#             component[CT[int(item[0])]] = int(item[1])
        data["data"].append(component)
    return json.dumps(data["data"])
    
@app.route('/table/', methods=['POST','GET'])
def table():
    return render_template('table.html')
    
@app.route('/table_2/', methods=['POST','GET'])
def table_2():
    return render_template('table_2.html')


if __name__ == '__main__':
    app.run()