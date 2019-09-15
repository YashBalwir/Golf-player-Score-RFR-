import flask
import numpy as np
from flask import Flask, render_template, request
import joblib
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
   return flask.render_template('index.html')

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method=='POST':
        arr = []
        arr.append(request.form["events_played"])
        arr.append(request.form["points"])
        arr.append(request.form["rounds_played"])
        arr.append(request.form["driving_dist"])
        arr.append(request.form["head_spd"])
        arr.append(request.form["angle"])
        arr.append(request.form["ball_spd"])
        arr.append(request.form["spin_rt"])
        arr.append(request.form["hang_tm"])
        arr.append(request.form["carry_dst"])
        arr.append(request.form["strokes"])
        arr.append(request.form["ttl_rounds"])
        arr = list(map(float,arr))
        arr = np.array(arr)

        prediction = model.predict(arr.reshape(1,-1))
        label = str(np.squeeze(prediction))
        return render_template('index.html', label=label)

if __name__ == '__main__':
    model = joblib.load('model.pkl')
    app.run(host='0.0.0.0', port=8000, debug=True)
