from flask import Flask, render_template
from flask import request

import json


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/goals/<goal>/")
def goal(goal):
    return render_template("goal.html")

@app.route("/profiles/<int:id>/")
def profile(id):
    with open('teachers.json') as json_file:
        profiles = json.load(json_file)
    return render_template("profile.html", id=id, profiles=profiles)

@app.route("/request/")
def request_select():
    return render_template("request.html")

@app.route("/request_done/")
def request_done():
    return render_template("request_done.html")

@app.route("/booking/<int:id>/<day>/<hour>/")
def booking(id, day, hour):
    with open('teachers.json') as json_file:
        profiles = json.load(json_file)
    return render_template("booking.html", id=id, day=day, hour=hour, profiles=profiles)

@app.route("/booking_done/", methods=['GET','POST'])
def booking_done():
    if request.method == 'POST':
        name = request.form['n']
        tel = request.form['t']
        return render_template("booking_done.html",name=name, tel=tel)


if __name__ == "__main__":
    app.run(debug=True)
