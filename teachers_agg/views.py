import json
import random

from flask import render_template, request
from sqlalchemy.sql.expression import func

from .data import goals
from teachers_agg import app, db
from teachers_agg.models import Teacher, Booking


@app.route("/")
def main():
    random_profiles = Teacher.query.order_by(func.random()).limit(6).all()
    return render_template("index.html", random_profiles=random_profiles)

@app.route("/goals/<goal>/")
def get_goal(goal):
    current_goal = goals[goal]
    profiles = get_teachers_profiles()
    return render_template("goal.html", goals=goals, goal=goal, current_goal=current_goal, profiles=profiles)

@app.route("/profiles/<int:id>/")
def profile(id):
    teacher = Teacher.query.get_or_404(id)
    teacher_free = json.loads(teacher.free)
    return render_template("profile.html", id=id, teacher=teacher, teacher_free=teacher_free)

@app.route("/request/")
def request_select():
    return render_template("request.html", goals=goals)

@app.route("/request_done/", methods=['GET', 'POST'])
def request_done():
    if request.method == 'POST':
        request_name = request.form.get('clientNameRequest')
        request_phone = request.form.get('clientPhoneRequest')
        goal = request.form.get('goal')
        time = request.form.get('time')
        request_data = {'name': request_name, 
                        'phone':request_phone,
                        'goal': goal,
                        'time': time
                        }
        with open('request.json', 'w') as f:
            request_data_json = json.dump(request_data, f)
        return render_template("request_done.html", request_data=request_data)

@app.route("/booking/<int:id>/<day>/<hour>/")
def booking(id, day, hour):
    profile = Teacher.query.get_or_404(id)
    return render_template("booking.html", id=id, day=day, hour=hour, profile=profile)

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
