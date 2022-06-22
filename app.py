from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home_page():
    return render_template('main.html')

@app.route('/math', methods=['POST'])

def math_operatoion():
    if(request.method == 'POST'):
        operation = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if (operation == 'add'):
            add = num1 + num2
            result = 'The sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(add)
        if (operation == 'Subtract'):
            sub = num1 - num2
            result = 'The Subtract of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(sub)
        if (operation == 'Multiplication'):
            multi = num1 * num2
            result = 'The Multiplication of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(multi)
        if (operation == 'Divide'):
            Divide = num1 / num2
            result = 'The Divide of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(Divide)
        return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)