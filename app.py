from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    s = "Hello, Haba!" + "\n" + \
        "Hello, Arsen!" + "\n" + \
        "Hello, Karim!" + "\n"
    return s
