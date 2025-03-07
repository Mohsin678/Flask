from flask import Flask


app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the mohsin home page"

@app.route("/index")
def index():
    return "This is our home page"

if __name__=="__main__":
    app.run(debug=True)