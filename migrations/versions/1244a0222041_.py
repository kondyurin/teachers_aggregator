"""empty message

Revision ID: 1244a0222041
Revises: 
Create Date: 2020-04-17 13:54:09.201948

"""
# import json

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1244a0222041'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('goal', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('goal', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('time', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('about', sa.String(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=False),
    sa.Column('picture_src', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('free', sa.String(), nullable=False),
    sa.Column('goal', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('day', sa.String(), nullable=False),
    sa.Column('hour', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers_goals',
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('goal_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['goal_id'], ['goals.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers_goals')
    op.drop_table('bookings')
    op.drop_table('teachers')
    op.drop_table('requests')
    op.drop_table('goals')
    # ### end Alembic commands ###
