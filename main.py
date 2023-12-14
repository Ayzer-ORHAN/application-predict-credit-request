import pickle
import numpy as np
import requests
from flask import Flask, render_template, request, jsonify
from pydantic import BaseModel, Field, PositiveFloat


app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict/", methods=["POST"])
def predict():

    # For rendering results on HTML GUI

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0],2)
    if output == 1 :
        credit = "accepted"
    else:
        credit = "refused"
    print (output)
    return render_template("prediction.html",prediction_text=f'Response to your credit request : Credit {credit}')

if __name__ == '__main__':
    app.debug = True
    print("salut")
    app.run(host='0.0.0.0', port=5000, debug=True)