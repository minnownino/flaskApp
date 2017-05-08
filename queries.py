import MySQLdb

def testQuery(SGA):
    mydb = MySQLdb.connect("localhost", "root", "root", "TDI")
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
    mydb = MySQLdb.connect("localhost", "root", "root", "TDI")
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
    mydb = MySQLdb.connect("localhost", "root", "root", "TDI")
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
    mydb = MySQLdb.connect("localhost", "root", "root", "TDI")
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
    mydb = MySQLdb.connect("localhost", "root", "root", "TDI")
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

def tumorALterditribution(SGA):
    '''
        get tumorset alteration distribution
        return (set_SM, set_CN_AMP, set_CN_DEL)
    '''
    mydb = MySQLdb.connect("localhost", "root", "root", "TDI")
    cursor = mydb.cursor()
    query = "select patient_id from Somatic_Mutations as S, Genes as G where S.gene_id = G.gene_id and G.gene_name = '%s'"%(SGA)
    cursor.execute(query)
    result_SM = cursor.fetchall()
    query = "select S.patient_id, S.gistic_score from SCNAs as S, Genes as G where S.gistic_score = 2 and S.gene_id = G.gene_id and G.gene_name = '%s'"%(SGA)
    cursor.execute(query)
    result_CN_AMP = cursor.fetchall()
    query = "select S.patient_id, S.gistic_score from SCNAs as S, Genes as G where S.gistic_score = -2 and S.gene_id = G.gene_id and G.gene_name = '%s'"%(SGA)
    cursor.execute(query)
    result_CN_DEL = cursor.fetchall()
    set_SM = set()
    set_CN_AMP = set()
    set_CN_DEL = set()
    for item in result_SM:
        set_SM.add(int(item[0]))
    for item in result_CN_AMP:
        set_CN_AMP.add(int(item[0])) 
    for item in result_CN_DEL:
        set_CN_DEL.add(int(item[0]))
    return (set_SM, set_CN_AMP, set_CN_DEL)

def getdriverAlterCTdistribution(SGA):
    '''
        get driver alteration cancer type distribution (significant)
    '''
    #split tumorset into different cancer types
    (SM, CN_AMP, CN_DEL) =  tumorALterditribution(SGA)
    SM_results = tumorCTdistribution(SM)
    CN_AMP_results = tumorCTdistribution(CN_AMP)
    CN_DEL_results = tumorCTdistribution(CN_DEL)
    return (SM_results, CN_AMP_results, CN_DEL_results)


def getTargetDEGlistBySGA(SGA):
    mydb = MySQLdb.connect("localhost", "root", "root", "TDI")
    cursor = mydb.cursor()
    query = "select DEG_name from SigSGADEGTumor where driver_gene_name = '%s'"%(SGA)
    cursor.execute(query)
    deglist = cursor.fetchall()
    
    
def getDEGlistAndCTdistribution(SGA):
    mydb = MySQLdb.connect("localhost", "root", "root", "TDI")
    cursor = mydb.cursor()
    query = "select DEG_name, count(*) from SigSGADEGTumor where driver_gene_name = '%s' group by DEG_name"%(SGA)
    cursor.execute(query)
    deglist = cursor.fetchall()
    data_CTdistribution = []
    # get tumor ct distribution, for tumors corresponding to each deg, their cancer type distribution
#     for deg in deglist:
#         query = "select P.cancer_type_id, count(*) from SigSGADEGTumor as S, Patients as P where S.driver_gene_name = '%s' and S.DEG_name = '%s' and S.tumor_name = P.name group by P.cancer_type_id"%('TP53', deg[0])
#         cursor.execute(query)
#         results = cursor.fetchall()
#         data_CTdistribution.append(results)
    return (data_CTdistribution, deglist)
    
def getTriplet(tumors, SGAs, DEGs):
    '''
        filter significant triplet by tumorset, SGAset and DEGset
        return filtered triplet
    '''
    #tumorset = '( '
    tumorset = '(' + ', '.join(repr(tumor) for tumor in tumors) + ')'
    tumorquery = 'tumor_name in %s'%(tumorset)
    #SGAset = '( '
    SGAset = '(' + ', '.join(repr(tumor) for tumor in SGAs) + ')'
    SGAquery = 'driver_gene_name in %s'%(SGAset)
    #DEGset = '( '
    DEGset = '(' + ', '.join(repr(tumor) for tumor in DEGs) + ')'
    DEGquery = 'DEG_name in %s'%(DEGset)
    querylist = []
    if len(tumors) != 0:
        querylist.append(tumorquery)
    if len(SGAs) != 0:
        querylist.append(SGAquery)
    if len(DEGs) != 0:
        querylist.append(DEGquery)
    mydb = MySQLdb.connect("localhost", "root", "root", "TDI")
    cursor = mydb.cursor()
    query = "select driver_gene_name, DEG_name, tumor_name from SigSGADEGTumor where " + " and ".join(querylist)
    #print query
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def checkSGAExistance(SGA):
    '''
        check input gene existance in SGAs table
    '''
    mydb = MySQLdb.connect("localhost", "root", "root", "TDI")
    cursor = mydb.cursor()
    query = "select count(*) from SGAs where SGA_name = '%s'"%(SGA)
    print query
    cursor.execute(query)
    result = cursor.fetchall()
    return int(result[0][0])
