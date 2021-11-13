from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

# def index():
# 	return "<h1>Hi there!</h1>"

def index():
	xy="Frank"
	return render_template("index.html", name=xy)

# localhost:5000/user/ruediger "<>" allows to pass in the name
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", name=name)

# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Invalid URL
@app.errorhandler(500)
def page_not_found(e):
	return render_template("404.html"), 500