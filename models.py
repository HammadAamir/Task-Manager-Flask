from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskTitle = db.Column(db.String(200), nullable=False)
    taskDate = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'Task: {self.taskTitle} created on {self.taskDate}'