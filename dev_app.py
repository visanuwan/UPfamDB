from flask import Flask, request, render_template, send_from_directory
from flask_restful import Resource, Api
import pandas as pd
import numpy as np
import h5py
import json


app = Flask(__name__, static_url_path='')
api = Api(app)

DF_87606 = pd.read_hdf("data/added_pfam_matrix_87606genomes.hdf", key="pfam_matrix")
DF_87606_sum = pd.DataFrame(DF_87606.sum())

DF_Pfam28 = pd.read_csv("data/Pfam-A.clans.tsv.mod", delimiter="\t", dtype=str)
DF_Pfam28.fillna("", inplace=True)

DF_87606_sum.index.name = "Pfam_accession"
DF_87606_sum.rename(columns={0: 'num_sum_org'}, inplace=True)
DF_87606_sum.reset_index(inplace=True)
DF_Pfam28_sum = pd.merge(DF_Pfam28, DF_87606_sum, on=['Pfam_accession'])


class Pfam_Meta(Resource):

    def get(self):
        return {'Number of Pfam': '16320', 'Number of Organism': '87606'}

class Core_Pfam(Resource):

    def get(self, number_org):
    	test_number = int(number_org)

    	# if test_number == 0:
    	# 	core_pfam = DF_87606_sum[DF_87606_sum == 0]
    	# else:
     #    	core_pfam = DF_87606_sum[DF_87606_sum >= test_number]
     #    num_core = len(core_pfam)

     #    pfam_detail = DF_Pfam28[DF_Pfam28.Pfam_accession.isin(core_pfam.index)].set_index('Pfam_accession').reset_index().to_dict(orient='records')

        if test_number == 0:
            # core_pfam = DF_87606_sum[DF_87606_sum == 0]
            pfam_detail = DF_Pfam28_sum[DF_Pfam28_sum.num_sum_org == 0].to_dict(orient='records')
        else:
            pfam_detail = DF_Pfam28_sum[DF_Pfam28_sum.num_sum_org >= test_number].to_dict(orient='records')
        num_core = len(pfam_detail)

        return {'num_core_pfam': num_core, 'pfam_data': pfam_detail}

class Dist_Pfam(Resource):

    def get_num_dist(self, pfam_acc):
        col = DF_87606[pfam_acc]
        num_dist = col[col == 1].shape[0]
        return num_dist

    def get(self, str_pfam):
        result_list = []
        pfam_acc_list = list(set(str_pfam.strip().split(',')))
        for pfam_acc in pfam_acc_list:
            pfam_dict = {}
            pfam_dict['pfam_acc'] = pfam_acc
            pfam_dict['num_organism'] = self.get_num_dist(pfam_acc)
            result_list.append(pfam_dict)
        # return json.dumps(result_list)
        return result_list		
 
api.add_resource(Dist_Pfam, '/api/distpfam/<str_pfam>')

api.add_resource(Core_Pfam, '/api/corepfam/<number_org>')

api.add_resource(Pfam_Meta, '/api')

@app.route('/')
def index_tem():
    return render_template('index.html')

@app.route('/corepfam.html')
def corepfam_tem():
    return render_template('corepfam.html')

@app.route('/distpfam.html')
def distpfam_tem():
    return render_template('distpfam.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

if __name__ == '__main__':
    # app.run(host= '0.0.0.0')
    app.run()
