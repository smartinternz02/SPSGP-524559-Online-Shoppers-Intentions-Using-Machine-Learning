import pickle

import numpy as np
import pandas as pd
from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)
model=pickle.load(open('rfmModelfin2.pkl','rb'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    admin=request.form['admin']
    adminduration = request.form['admin-duration']
    info = request.form['info']
    infoduration = request.form['info-duration']
    productrelated= request.form['product-related']
    productRelatedDuration = request.form['product-related-duration']
    bouncerates = request.form['bounce-rates']
    exitrates = request.form['exit-rates']
    pagevalues = request.form['page-values']
    specialday=request.form['special-day']
    os= request.form['os']
    browser = request.form['browser']
    region = request.form['region']
    traffictype = request.form['traffic-type']
    weekend = request.form['weekend']
    month_encoded = request.form['month']
    VisitorType_encoded = request.form['visitor-type']

    df2=pd.DataFrame([{"Administrative":admin,
                      "Administrative_Duration":adminduration,
                      "Informational":info,
                      "Informational_Duration": infoduration ,
                      "ProductRelated":productrelated,
                      "ProductRelated_Duration":productRelatedDuration,
                      "BounceRates":bouncerates,
                      "ExitRates":exitrates,
                      "PageValues":pagevalues,
                      "SpecialDay": specialday,
                      "OperatingSystems":os,
                      "Browser": browser,
                      "Region":region,
                      "TrafficType":traffictype,
                      "Weekend":bool(weekend),
                      "month_encoded ":month_encoded ,
                      "VisitorType_encoded": VisitorType_encoded


                      }])

    print(df2.T)
    out=model.predict(df2)

    if out[0]==False:
        ot="Not buy the goods"
    elif out[0]==True:
        ot="Buy the goods"



    return render_template('pass.html',op=ot)
if __name__=="__main__":
    app.run(debug=True)