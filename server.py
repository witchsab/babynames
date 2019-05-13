from flask import Flask, render_template
from home import homeapi


app = Flask(__name__)

app.register_blueprint(homeapi)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check")
def check():
    return "Checked. Server is responding."


if __name__ == "__main__":
    app.run(debug=True)
