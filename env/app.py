from flask import Flask,request,jsonify
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import os 

model = pickle.load(open('C:/Users/Usuario/Documents/TFG/Futpool/data/futpool','rb')) 
app = Flask(__name__)

@app.route('/predict',methods=['POST']) 
def predict(): 
    p5l = request.form.get('PuntosLocalUltimas5Jornadas') 
    g5l = request.form.get ('GolesFavorLocalUltimas5Jornadas') 
    g5lc = request.form.get('GolesContraLocalUltimas5Jornadas') 
    p5v = request.form.get('PuntosVisitanteUltimas5Jornadas') 
    g5v = request.form.get('GolesFavorVisitanteUltimas5Jornadas') 
    g5lv = request.form.get('GolesContraVisitanteUltimas5Jornadas') 
     
    input_query = np.array([[p5l,g5l,g5lc,p5v,g5v,g5lv]]) 
    result = model.predict(input_query)[0] 
    return jsonify({'placement ':str(result)}) 
if __name__ == '__main__': 
    app.run(debug=True)