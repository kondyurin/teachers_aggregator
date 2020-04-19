import json

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.exc import IntegrityError
# from sqlalchemy import create_engine
# from sqlalchemy.engine import reflection


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


# engine = create_engine(db_path)

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


# add_teachers_to_db()
# add_goals_to_db()

# db.drop_all()

# def is_db_empty():
#     table_names = reflection.Inspector.from_engine(engine).get_table_names()
#     print(table_names)
#     is_empty = table_names == []
#     is_empty = engine.has_table('Teacher')

# is_db_empty()