from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/stock/")
def stock():
    return render_template("stock.html")

app.run(debug=True,port=80)