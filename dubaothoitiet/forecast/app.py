from flask import Flask, render_template, request, jsonify
from calculation import process_inputs

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        inputs = [
            data['date'],
            data['precipitation'],
            data['temp_max'],
            data['temp_min'],
            data['wind']
        ]
        result = process_inputs(inputs)
        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
