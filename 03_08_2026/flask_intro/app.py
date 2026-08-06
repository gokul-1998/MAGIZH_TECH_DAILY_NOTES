
from flask import Flask,render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    data={"message": "Hello all india"}
    return render_template("index.html", data=data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run()