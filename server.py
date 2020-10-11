import pickle
from flask import Flask,request
import numpy as np
from flasgger import Swagger
import json
from model import TfidfModel

class Server:
    def __init__(self):
        with open('./rf.pkl','rb') as model_file:
            self._model = pickle.load(model_file)
        

    def run(self):
        app = Flask(__name__)
        swagger = Swagger(app)
        @app.route('/predict')
        def predict_movie():
            """Example endpoint returning movie recommendation
            ---
            parameters:
                -  name: title
                   in: query
                   required: true
            """
            title = request.args.get("title")
            recomm = TfidfModel().recommender(self._model,title)
            return recomm.to_json()
        app.run(host='0.0.0.0',port=5000)