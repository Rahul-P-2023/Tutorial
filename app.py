from flask import *
import pandas as pd
import pickle

model=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict',methods=['POST','GET'])
def predit():
    if request.method=='POST':
        dep_time=request.form['Dept_Time']
        
        Journey_day=pd.to_datetime(dep_time,format='%Y-%m-%dT%H:%M').day
        Journey_month=pd.to_datetime(dep_time,format='%Y-%m-%dT%H:%M').month

        Departure_hour=pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").hour
        Departure_min=pd.to_datetime(dep_time,format="%Y-%m-%dT%H:%M").minute
        arrival_time=request.form['Arrival_Time']
        Arrival_hour=pd.to_datetime(arrival_time,format="%Y-%m-%dT%H:%M").hour
        Arrival_min=pd.to_datetime(arrival_time,format="%Y-%m-%dT%H:%M").minute

        total_Stops=int(request.form['stops'])
        airline=request.form['airline']
        Air,d,s=0,0,0
        if airline=='Air Asia':
            Air=0
        elif airline=="Air India":
            Air=1
        elif airline=="GoAir":
            Air=2
        elif airline=="IndiGo":
            Air=3
        elif airline=="SpiceJet":
            Air=8
        elif airline=="Multiple carriers":
            Air=6
        elif airline=="Multiple carries Premium economy":
            Air=7
        elif airline=="Jet Airways":
            Air=4
        elif airline=="Jet Airways Bussiness":
            Air=5
        elif airline=="Visrata":
            Air=10
        Source=request.form['Source']
        if Source=='Delhi':
            s=2
        elif Source=='Kolkata':
            s=3
        elif Source=="Mumbai":
            s=4
        elif Source=="Chennai":
            s=1
        else:
            s=0
        destination=request.form['Destination']
        if destination=="Delhi":
            d=2
        elif destination=="Hydrabad":
            d=4
        elif destination=="Kolkata":
            d=3
        elif destination=="Cochin":
            d=1
        else:
            d=0

        output=model.predict([[total_Stops,d,s,Air,Journey_day,Journey_month,Departure_hour,Departure_min,Arrival_hour,Arrival_min]])
        return render_template("main.html",pred=output)

if __name__=='__main__':
    app.run(debug=True)
    
