from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import numpy as np
import h5py


app = Flask(__name__)
api = Api(app)

DF_87606 = pd.read_hdf("/Users/visanuwan/ORNL/BSDHIGHMEM/PfamA70k/Dec312015/added_pfam_matrix_87606genomes.hdf", key="pfam_matrix")
DF_87606_sum = DF_87606.sum()


class Pfam_Meta(Resource):
    def get(self):
        return {'Number of Pfam': '16320', 'Number of Organism': '87606'}

class Core_Pfam(Resource):
    def get(self, number_org):
        num_core = len(DF_87606_sum[DF_87606_sum > number_org])
        return {'Number of Organisms': num_core}
 
api.add_resource(Core_Pfam, '/corepfam/<int:number_org>')

api.add_resource(Pfam_Meta, '/')

if __name__ == '__main__':
    app.run()
