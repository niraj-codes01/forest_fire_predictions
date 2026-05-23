import pickle
from flask import Flask,request,jsonify,render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

##import ridge regressor and standard scaler pickle
ridge_model = pickle.load(open('models/ridge.pkl','rb'))
standard_scaler = pickle.load(open('models/scaler.pkl','rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    if request.method =="POST":
        data = request.form
        Temperature = float(data.get('Temperature'))
        RH = float(data.get('RH'))
        Ws = float(data.get('Ws'))
        Rain = float(data.get('Rain'))
        FFMC = float(data.get('FFMC'))
        DMC = float(data.get('DMC'))
        #DC = float(data.get('DC'))       # new
        ISI = float(data.get('ISI'))
        #BUI = float(data.get('BUI'))     # new
        Classes = float(data.get('Classes'))
        Region = float(data.get('Region'))  # or encode if categorical

        input_df = pd.DataFrame([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]],
                                columns=['Temperature','RH','Ws','Rain','FFMC','DMC','ISI','Classes','Region'])

        new_data_scaled = standard_scaler.transform(input_df)
        result = ridge_model.predict(new_data_scaled)


        return render_template('home.html',results=result[0])

    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")