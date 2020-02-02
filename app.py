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
        teacher_id = request.form.get('clientTeacher')
        name = request.form.get('clientName')
        phone = request.form.get('clientPhone')
        day = request.form.get('clientWeekday')
        hour = request.form.get('clientTime')
        booking_data = {'id': teacher_id, 'name':name, 'phone': phone, 'day': day, 'hour': hour}
        with open('booking.json', 'w') as f:
            booking_data_json = json.dump(booking_data, f)
        return render_template("booking_done.html", booking_data=booking_data)


if __name__ == "__main__":
    app.run(debug=True)
