import flask
import os
from flask import Flask, request, render_template
import json
from main import load_dependency, predict_type


app = Flask(__name__, static_url_path='/static')
model, lblencoder, scaler = None, None, None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['post'])
def get_prediction():
    try:
        s_length = request.json["sepal_length"]
        s_width = request.json["sepal_width"]
        p_length = request.json["petal_length"]
        p_width = request.json["petal_width"]
        category = predict_type([s_length, s_width, p_length, p_width], scaler, lblencoder, model)

        res = {'category': category}
        return app.response_class(response=json.dumps(res), status=200, mimetype='application/json')
    except Exception as error:
        err = str(error)
        print(err)
        return app.response_class(response=json.dumps(err), status=500, mimetype='application/json')


if __name__ == '__main__':
    model, lblencoder, scaler = load_dependency()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
