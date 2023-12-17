from flask import Flask, request, jsonify
from calculator import Calculator  # Import your Calculator class from calculator.py

app = Flask(__name__)

calc = Calculator()

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data['expression']

        tokens = calc.tokenize_expression(expression)
        rpn_expression = calc.shunting_yard_algorithm(tokens)
        result = calc.calculate_rpn(rpn_expression)

        response = {'result': result}
        return jsonify(response), 200
    except ValueError as e:
        response = {'error': str(e)}
        return jsonify(response), 400
    except Exception as e:
        response = {'error': 'An error occurred while processing the request'}
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(debug=True)
