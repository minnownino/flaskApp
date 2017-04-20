import MySQLdb

def testQuery(SGA):
    mydb = MySQLdb.connect("localhost", "", "", "TDI")
    cursor = mydb.cursor()
    query = "SELECT * FROM SigSGADEGTumor where driver_gene_name = '%s'"%(SGA)
    cursor.execute(query)
    result = cursor.fetchall()
    degs = []
    if len(result) == 0:
        return degs
    else:
        for row in result:
            degs.append(row[6])
        return degs


def getSGAtumorAll(SGA):
    '''
        get tumorset where SGA exists
    '''
    mydb = MySQLdb.connect("localhost", "", "", "TDI")
    cursor = mydb.cursor()
    query = " select S.patient_id from SGAs as S, Genes as G where S.gene_id = G.gene_id and G.gene_name = '%s'"%(SGA)
    cursor.execute(query)
    results = cursor.fetchall()
    tumorset = set()
    for result in results:
        tumorset.add(result[0])
    return tumorset
def getSGAtumordriver(SGA):
    '''
        get tumorset where SGA is driver
    '''
    mydb = MySQLdb.connect("localhost", "", "", "TDI")
    cursor = mydb.cursor()
    query = " select T.patient_id from TDI_driverCallPerTumor as T, Genes as G where T.gene_id = G.gene_id and G.gene_name = '%s'"%(SGA)
    cursor.execute(query)
    results = cursor.fetchall()
    tumorset = set()
    for result in results:
        tumorset.add(result[0])
    return tumorset

def getCT():
    '''
        get tumor types, save into disctionary
    '''
    mydb = MySQLdb.connect("localhost", "", "", "TDI")
    cursor = mydb.cursor()
    query = "select cancer_type_id, abbv from Cancer_Types"
    cursor.execute(query)
    results = cursor.fetchall()
    cancer_types = {}
    for result in results:
        #print result[0], result[1]
        cancer_types[result[0]] = result[1]
    return cancer_types

def tumorCTdistribution(tumors):
    '''
        get tumorset cancer type distribution
    '''
    mydb = MySQLdb.connect("localhost", "", "", "TDI")
    cursor = mydb.cursor()
    tumorset = '( '
    tumorset = '(' + ', '.join(str(tumor) for tumor in tumors) + ')'
    query = "select cancer_type_id, count(*) from Patients where patient_id in %s group by cancer_type_id"%(tumorset)
    cursor.execute(query)
    results = cursor.fetchall()
    return results

def getSGACTdistribution(SGA):
    '''
        get cancer type distribution and cancer types data
    '''
    tumorset_all = getSGAtumorAll(SGA)
    tumorset_driver = getSGAtumordriver(SGA)
    all_distribution = tumorCTdistribution(tumorset_all)
    driver_distribution = tumorCTdistribution(tumorset_driver)
    cancer_types = getCT()
    return (all_distribution, driver_distribution, cancer_types)