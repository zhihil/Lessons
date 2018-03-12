from flask import Flask, request, render_template

app = Flask(__name__)

OK = "200"
BAD_REQUEST = "400"
SERVER_ERROR = "500"

@app.route('/')
def index():
    return render_template('archery.html')

@app.route('/score', methods=["GET", "POST"])
def uploadScore():
    if request.method == "POST":
        data = request.data

        # TODO: process data.

        return OK

    elif request.method == "GET":
        return render_template('archery.html'), OK
