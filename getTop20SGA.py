import MySQLdb
import json

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

# read files
df = pd.read_csv('driverCallPerTumor2017-07-10-1.csv')
# top 20 SGA
grouped = df.groupby(df.cause_gene_name).size()
sgatop20 = [x for x in grouped.nlargest(20).index]

sgadata = dict()
for sga in sgatop20:
    (set_SM, set_CN_AMP, set_CN_DEL) = tumorALterditribution(sga)
    results = tumorCTdistribution(set_SM)
    results2 = tumorCTdistribution(set_CN_AMP)
    results3 = tumorCTdistribution(set_CN_DEL)
    results1 = dict((int(x), int(y)) for x, y in results)
    results2 = dict((int(x), int(y)) for x, y in results2)
    results3 = dict((int(x), int(y)) for x, y in results3)
    sga_list = dict()
    for i in xrange(17):
        sga_list[i] = []
        sga_list[i] = [results1.get(i, 0)]
        sga_list[i].append(results2.get(i, 0) + sga_list[i][0])
        sga_list[i].append(results3.get(i, 0) + sga_list[i][1])
    sgadata[sga] = sga_list

json.dumps(sgadata)