from flask import Flask, render_template, request, json, url_for, Response, make_response, send_file, flash
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
#from flask_mysqldb import MySQL
from queries import *
import csv

app = Flask(__name__)
app.secret_key = 'my unobvious secret key'
mysql = MySQL(app)
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = ''
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

@app.route('/search/')
def search():
    #flash("flash test!!!!")
    return render_template('search.html')

@app.route('/layout/', methods=['POST', 'GET'])
def test():
    SGA = request.form['SGA']
    # check SGA existance in our database
    if checkSGAExistance(SGA) == 0:
        flash("The gene " + SGA + " is not yet in our database, try another one. Please search in the future or contact us for more information.")
        return render_template('search.html')
    # prepare data for driver/SGA plot
    (all_distribution, driver_distribution, cancer_types) = getSGACTdistribution(SGA)
    all_distribution = list(int(i[1]) for i in all_distribution)
    driver_distribution = list(int(i[1]) for i in driver_distribution)
    # prepare data for sm & cn plot
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
    return render_template('result_all.html',  all_distribution = all_distribution, driver_distribution = driver_distribution, cancer_types = cancer_types, SGA=SGA.upper())
    
@app.route('/')
def main():
    (all_distribution, driver_distribution, cancer_types) = getSGACTdistribution('MUC6')
    all_distribution = list(int(i[1]) for i in all_distribution)
    driver_distribution = list(int(i[1]) for i in driver_distribution)
    return render_template('index.html', all_distribution = all_distribution, driver_distribution = driver_distribution, cancer_types = cancer_types)
    
    #return render_template('index.html')

@app.route('/getTripletCSV/', methods=['GET','POST'])
def getTripletCSV():
    import csv
    SGAs = request.form['SGAs']
    DEGs = request.form['DEGs']
    tumors = request.form['Tumors']
    print SGAs
    print DEGs
    print tumors
    if tumors is not None:
        tumors = str(tumors).split(',')
    else:
        tumors = []
    if SGAs is not None:
        SGAs = str(SGAs).split(',')
    else:
        SGAs = []
    if DEGs is not None:
        DEGs = str(DEGs).split(',')
    else:
        DEGs = []
    result = getTriplet(tumors, SGAs, DEGs)
    with open("out.csv", "wb") as csv_file:              # Python 2 version
        csv_writer = csv.writer(csv_file)
        csv_writer = csv.writerow(["SGAname", "DEGname", "Tumorname"])
        csv_writer.writerows(result)
    #return_file = open("out.csv", 'r')
    #csv = '1,2,3\n4,5,6\n'
    #response = make_response(return_file)
    #response.mimtype = 'text/csv'
    #response.headers['Content-Disposition'] = 'attachment; filename=out.csv'
    return send_file('out.csv', attachment_filename='out.csv')

@app.route('/getTripletTEST')
def getTripletTEST():
    csv = '1,2,3\n4,5,6\n'
    return Response(csv, mimetype='text/csv', headers={"Content-disposition": "attachment; filename=myplot.csv"})

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
