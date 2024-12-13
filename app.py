from flask import Flask,render_template,request
import pickle
import numpy as np




# 1.created object for class Flask
app=Flask(__name__)

# loading model--model should contain only numbers
with open("scaler.pkl","rb")as f:
    ss=pickle.load(f)

with open("model.pkl","rb")as f:
    rfc=pickle.load(f)

#7.
def predict_health(Soil_Moisture=15.336156, Ambient_Temperature=21, Soil_Temperature=15,Humidity=55, Light_Intensity=650, Soil_pH=29, Nitrogen_Level=50, Phosphorus_Level=25,
                 Potassium_Level=30, Chlorophyll_Content=45, Electrochemical_Signal=1):
    temp_array = list()

    #Soil_Moisture
    temp_array=temp_array+[Soil_Moisture]

    #Ambient_Temperature
    temp_array=temp_array+[Ambient_Temperature]
    temp_array=temp_array+[Soil_Temperature]

    #Humidity
    temp_array=temp_array+[Humidity]

    #Light_Intensity
    temp_array=temp_array+[Light_Intensity]

    #Soil_pH
    temp_array=temp_array+[Soil_pH]

    #Nitrogen_Level
    temp_array=temp_array+[Nitrogen_Level]

    #Phosphorus_Level
    temp_array=temp_array+[Phosphorus_Level]

    #Potassium_Level
    temp_array=temp_array+[Potassium_Level]

    #Chlorophyll_Content
    temp_array=temp_array+[Chlorophyll_Content]

    #Electrochemical_Signal
    temp_array=temp_array+[Electrochemical_Signal]

#converting into numpy array
    temp_array= np.array([temp_array])
    print(temp_array)
    temp_array=ss.transform(temp_array)
    pred=rfc.predict(temp_array)
    print(pred)
    if pred[0]==0:
        result='Healthy Plant'
    elif pred[0]==1:
        result='Moderate Stress'
    else:
        result="High Stress"

    #prediction
    return result
        




# 3.creating router
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html') 

# 4.
@app.route("/predict",methods=['POST','GET'])

def predict():
    if request.method=='POST':
        Soil_Moisture=float(request.form.get('Soil_Moisture'))
        Ambient_Temperature=float(request.form.get('Ambient_Temperature'))
        Soil_Temperature=float(request.form.get('Soil_Temperature'))
        Humidity=float(request.form.get('Humidity'))
        Light_Intensity=float(request.form.get('Light_Intensity'))
        Soil_pH=float(request.form.get('Soil_pH'))
        Nitrogen_Level=float(request.form.get('Nitrogen_Level'))
        Phosphorus_Level=float(request.form.get('Phosphorus_Level'))
        Potassium_Level=float(request.form.get('Potassium_Level'))
        Chlorophyll_Content=float(request.form.get('Chlorophyll_Content'))
        Electrochemical_Signal=float(request.form.get('Electrochemical_Signal'))
        
        print(type(Electrochemical_Signal))
        health=predict_health(Soil_Moisture=Soil_Moisture, Ambient_Temperature=Ambient_Temperature, Soil_Temperature=Soil_Temperature,
                            Humidity=Humidity, Light_Intensity=Light_Intensity, Soil_pH=Soil_pH, Nitrogen_Level=Nitrogen_Level, Phosphorus_Level=Phosphorus_Level,
                 Potassium_Level=Potassium_Level, Chlorophyll_Content=Chlorophyll_Content, Electrochemical_Signal=Electrochemical_Signal)
        print(health)
        return render_template('result.html',prediction=health)


    return render_template('predict.html') 

@app.route("/contact")
def contact():
    return render_template('contact.html') 









#2. to create main function
if __name__=='__main__':
    # running server
    app.run(debug=True)