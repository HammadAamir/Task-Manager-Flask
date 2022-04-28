from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    taskTitle = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Save Task')

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Yes')