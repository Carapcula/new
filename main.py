from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main")
def maining():
    return '<h1>Hello, Worssssld!</h1>'

    
app.run(debug=True)