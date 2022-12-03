from evaluation import calculator
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def calculate():
    expression = request.form.get("exp")
    result = calculator(expression)
    return render_template('index.html', result=str(result))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
