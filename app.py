from flask import Flask, render_template,request,jsonify, url_for
import pickle
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
     return render_template('Home.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        
        z_table = pickle.load(open('z_table.pkl','rb'))
    
        z_table['PLANE_AGE'] = request.form['PLANE_AGE']
        z_table['LATITUDE'] = request.form['LATITUDE']
        z_table['LONGITUDE'] = request.form['LONGITUDE']
        z_table['AIRPORT_FLIGHTS_MONTH'] = request.form['AIRPORT_FLIGHTS_MONTH']
        z_table['CONCURRENT_FLIGHTS'] = request.form['CONCURRENT_FLIGHTS']
        z_table['AIRLINE_AIRPORT_FLIGHTS_MONTH']=request.form['AIRLINE_AIRPORT_FLIGHTS_MONTH']
        z_table['AVG_MONTHLY_PASS_AIRPORT']=request.form['AVG_MONTHLY_PASS_AIRPORT']
        z_table['PRCP']=request.form['PRCP']
        z_table['TMAX']=request.form['TMAX']
        z_table['AWND']=request.form['AWND']
        
        dist = request.form['DISTANCE_GROUP']
        seg = request.form['SEGMENT_NUMBER']
        z_table[dist] = 1
        z_table[seg] = 1


        z_table = z_table.astype('float')
        
        model = pickle.load(open('model.pkl','rb'))

        result = model.predict(z_table)[0]
        
        if result == 1:
            output = "Flight may delay more than 15 min"
            
        else:
            output = "Flight may not delay more than 15 min"

        return render_template("Home1.html",result=output,dist=dist,seg=seg)

if __name__ == "__main__":
    #app.debug = True
    app.run()
