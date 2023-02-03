from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from datetime import datetime
from . import db
from .models import User, Department
import os

data_department = Blueprint('data_department', __name__)

@data_department.route('/data/departments')
@login_required
def departments():
    parentDepartments = Department.query.filter_by(active=True).all()

    return render_template('data/departments/list.html', 
        departments=parentDepartments, 
        parentDepartments=parentDepartments)

@data_department.route('/data/department/new')
@login_required
def department_new():

    # Selects
    parentDepartments = Department.query.filter().all()

    return render_template('data/departments/form-new.html', 
        parentDepartments=parentDepartments)

@data_department.route('/data/department/new', methods=['POST'])
@login_required
def department_new_post():
    name = request.form.get('name')
    parentDepartmentValue = request.form.get('parentDepartmentSelect',type=int)

    if parentDepartmentValue == 0:
        parentDepartmentValue = None

    new_department = Department(
        name=name, 
        parent_id=parentDepartmentValue,
        active=True,
        creation_date=datetime.now(), 
        update_date=None)

    # add the new user to the database
    db.session.add(new_department)
    db.session.commit()

    return redirect(url_for('data_department.departments'))

@data_department.route('/data/department/edit')
@login_required
def department_update():
    return render_template('/data/departments/form-edit.html')

@data_department.route('/data/department/edit', methods=['POST'])
@login_required
def department_update_post():
    return redirect(url_for('data_department.departments'))

@data_department.route('/data/department/delete', methods=['POST'])
@login_required
def department_delete_post():
    return redirect(url_for('data_department.departments'))