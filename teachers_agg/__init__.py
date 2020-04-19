import json

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.exc import IntegrityError


app = Flask(__name__)

db_path = 'sqlite:///db.db'
app.secret_key = 'abrikos'
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from teachers_agg.data import goals
from teachers_agg import views, models
from teachers_agg.models import Teacher, Goal


def add_teachers_to_db():
    """
    Add teachers from teachers.json to teachers table.
    """
    with open('teachers_agg/teachers.json') as json_file:
        profiles = json.load(json_file)
    for item in profiles['teachers']:
        teacher = Teacher(id=item['id'], 
                          name=item['name'],
                          about=item['about'],
                          rating=item['rating'],
                          picture_src=item['picture'],
                          price=item['price'],
                          free=json.dumps(item['free']),
                          goal=','.join(item['goals']))
        db.session.add(teacher)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()


def add_goals_to_db():
    """
    Add goals from data.py to goals table.
    """
    for name, value in goals.items():
        goal = Goal(goal=name, value=value)
        db.session.add(goal)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()


def complete_teachers_goals_table():
    """
    Complete m2m association table.
    """
    teachers = Teacher.query.all()
    for teacher in teachers:
        goals = teacher.goal.split(',')
        for item in goals:
            goal = Goal.query.filter(Goal.goal == item).first()
            teacher.goals.append(goal)
        db.session.commit()


# add_teachers_to_db()
# add_goals_to_db()
# complete_teachers_goals_table()