from flask import Flask, render_templates, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_templates('calculator.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    number1 = int(request.form['number1'])
    number2 = int(request.form['number2'])
    operation = request.form['operation']
    result = None

    if operation == "+":
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2
    elif operation == '/':
        result = number1 / number2
    elif operation == '**':
        result = pow(number1, number2)
    elif operation == 'square':
        result = math.sqrt(number1)

    return render_templates('result.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
