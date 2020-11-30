from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():

	s = ["Hello, Haba!",
		"Hello, Arsen!",
		"Hello, Karim!"]

	out = "<pre>{}</pre>".format("\n".join(s))
	return out


@app.route('/user/<username>/<iq>')
def hello_haba(username, iq):

	s = []

	for i in range(100):
		s.append(username+str(iq*2)+"iq")

	out = "<pre>{}</pre>".format("\n".join(s))
	return out

app.debug = True
app.run()