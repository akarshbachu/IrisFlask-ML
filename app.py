import sklearn
import sklearn.datasets
import sklearn.ensemble
import pickle
#from jsonify import convert
from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import json


pickle_in =  open('iris_rf_model','rb')
rf = pickle.load(pickle_in)
pickle_in.close()

app = Flask(__name__)

@app.route("/",methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/predict",methods=['POST'])
def predict():
    # data = request.get_json(force=True)
    # print(type(data))
    # #data_li = [data['sl'],data['sw'],data['pl'],data['pw']]
    # pred = rf.predict(np.array([data['sl'],data['sw'],data['pl'],data['pw']]).reshape(1,-1))[0] 
    # print(rf.predict(np.array([data['sl'],data['sw'],data['pl'],data['pw']]).reshape(1,-1)))
    # return jsonify(Class=str(pred))
    sepallength = float(request.form['SepalLength'])
    sepalwidth = float(request.form['SepalWidth'])
    petallength = float(request.form['PetalLength'])
    petalwidth = float(request.form['PetalWidth'])
    labelFlower = {0:'Setosa', 1:'Virginica', 2:'VersiColor'}
    pred = rf.predict(np.array([sepallength,sepalwidth,petallength,petalwidth]).reshape(1,-1))[0]
    
    return render_template("home.html",result=labelFlower.get(pred,'Unidentified'))

if __name__ == "__main__":
    app.run(debug=False,port=5000)


