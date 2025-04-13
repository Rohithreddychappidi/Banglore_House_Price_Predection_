from flask import Flask, request, jsonify
import util





app = Flask(__name__)
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')


# Load the model and columns before serving any request
util.load_saved_route()

@app.route('/Get_Location_Names')
def Get_Location_Names():
    response = jsonify({
        'Locations': util.Get_Location_Names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    data = request.get_json()  # This works only if Content-Type is application/json
    total_sqft = float(data['total_sqft'])
    location = data['Location']
    bhk = int(data['bhk'])
    bath = int(data['bath'])

    response = jsonify({
        'estimated_price': util.Get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask server for Home Price Prediction...")
    app.run()
