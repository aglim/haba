from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():

    s = ["Hello, Haba!",
        "Hello, Arsen!",
        "Hello, Karim!"]

    out = "<pre>{}</pre>".format("\n".join(s))
    return out


if __name__ == '__main__':
    app.run()
