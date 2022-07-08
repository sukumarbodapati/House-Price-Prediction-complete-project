from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_location_names', methods=['GET'])
def get_locations():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_house_prices():

    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_prices(location, total_sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask")
    util.load_saved_artifacts()
    app.run()
