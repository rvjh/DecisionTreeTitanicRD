import pickle
from flask import Flask,request,render_template
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier


app=Flask(__name__)
@app.route('/',methods=['GET'])

def homepage():
    return render_template('home.html')

@app.route('/predict', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        try:
            data1 = float(request.form['a'])
            data2 = float(request.form['b'])
            data3 = float(request.form['c'])
            data4 = float(request.form['d'])
            arr = np.array([[data1, data2, data3, data4]])
            filename = 'clf3_grid.sav'
            loaded_model = pickle.load(open(filename, 'rb'))  # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict(arr)
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('after.html', data=prediction)
        except Exception as e:
            print('The Exception message is: ',e)
            return 'Opps!! you are supposed to give number not character..'

    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run()