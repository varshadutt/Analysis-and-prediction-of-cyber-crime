import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('cycrmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/analysis')
def analysis():
    return render_template('crimeanalysis.html')

@app.route('/output')
def out():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('admin.html')

@app.route('/reg')
def register():
    return render_template('reg.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = int(prediction[0])
    
    return render_template('index.html', prediction_text='{} crime cases are to be expected.'.format(output))

@app.route('/results',methods=['GET/POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)