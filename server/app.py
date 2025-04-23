#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string_param>")
def print_string(string_param):
    print(string_param)
    return string_param

@app.route("/count/<int:int_param>")
def count_int(int_param):
    result = ""
    for i in range(int_param):
        result += f"{i}\n"
    return result

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 == 0:
            return "Cannot divide by zero!"
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Unsupported operation"
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
