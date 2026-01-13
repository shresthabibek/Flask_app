from flask import Flask

# main variable to use.
app = Flask(__name__)

# start creating end-points.

@app.route("/", methods=['GET'])
def hello():
    return "Hello there.!!"

@app.route("/ping", methods=['GET'])
def ping():
    return {"message" : "why are you pinging me?"}
