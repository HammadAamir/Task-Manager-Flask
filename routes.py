from app import app, db
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from models import Task
from datetime import datetime

import forms

@app.route('/')
@app.route('/index')
def index():
    allTasks = Task.query.all()
    return render_template('index.html', siteTitle='Best Title', tasks=allTasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    addForm = forms.AddTaskForm()
    if addForm.validate_on_submit():
        print('Submit Title', addForm.taskTitle.data)
        taskEntered = Task(taskTitle=addForm.taskTitle.data, taskDate=datetime.utcnow())
        db.session.add(taskEntered)
        db.session.commit()
        flash('Task added Successfully')
        return redirect(url_for('index'))
    return render_template('add.html', form=addForm)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    editForm = forms.AddTaskForm()
    if task:
        if editForm.validate_on_submit():
            task.taskTitle = editForm.taskTitle.data
            task.taskDate = datetime.utcnow()
            db.session.commit()
            flash('Task has been updated successfully!')
            return redirect(url_for('index'))
        editForm.taskTitle.data = task.taskTitle
        return render_template('edit.html', form=editForm, task_id=task_id)
    else:
        flash('Task not found.')
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    deleteForm = forms.DeleteTaskForm()
    if task:
        if deleteForm.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been deleted successfully!')
            return redirect(url_for('index'))
        return render_template('delete.html', form=deleteForm, task_id=task_id,title=task.taskTitle)
    else:
        flash('Task not found.')
    return redirect(url_for('index'))