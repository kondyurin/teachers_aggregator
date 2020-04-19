from teachers_agg import db


teachers_goals = db.Table('teachers_goals',
                          db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id')),
                          db.Column('goal_id', db.Integer, db.ForeignKey('goals.id'))
                          )


class Teacher(db.Model):
    __tablename__ = 'teachers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    about = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    picture_src = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    free = db.Column(db.String, nullable=False)
    goal = db.Column(db.String, nullable=False)
    booking = db.relationship('Booking', back_populates='teacher')
    goals = db.relationship('Goal', secondary='teachers_goals', back_populates='teachers')


class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    day = db.Column(db.String, nullable=False)
    hour = db.Column(db.Integer, nullable=False)
    teacher = db.relationship('Teacher', back_populates='booking')
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))


class Goal(db.Model):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)
    teachers = db.relationship('Teacher', secondary='teachers_goals', back_populates='goals')


class Request(db.Model):
    __tablename__ = 'requests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    goal = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)