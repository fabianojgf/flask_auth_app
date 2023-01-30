from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from datetime import datetime
from . import db
from .models import User, Permission, PermissionType, PermissionStatus, Department
import os

permission = Blueprint('permission', __name__)

@permission.route('/account/permissions')
@login_required
def account_permissions():
    permissions = Permission.query.filter_by(
        user_id=current_user.id, permission_type_id=3, active=True).all()
    permissions_sol = Permission.query.filter_by(
        user_id=current_user.id, permission_type_id=1, active=True).all()
    permissions_other = Permission.query.filter(
        Permission.user_id==current_user.id, Permission.permission_type_id>=2, Permission.active==True).all()

    # Selects
    permissionTypes = PermissionType.query.filter().all()
    departments = Department.query.filter().all()

    return render_template('account/permissions/list.html', 
        permissions=permissions, 
        permissions_sol=permissions_sol, 
        permissions_other=permissions_other,
        permissionTypes=permissionTypes,
        departments=departments)

@permission.route('/account/permissions/new')
@login_required
def account_permission_new():

    # Selects
    permissionTypes = PermissionType.query.filter().all()
    departments = Department.query.filter().all()

    return render_template('account/permissions/form-new.html',
        permissionTypes=permissionTypes,
        departments=departments)

@permission.route('/account/permissions/new', methods=['POST'])
@login_required
def account_permission_new_post():
    return render_template(url_for('department.account_permissions'))

@permission.route('/account/permissions/edit')
@login_required
def account_permission_update():
    return render_template('account/permissions/form-edit.html')

@permission.route('/account/permissions/edit', methods=['POST'])
@login_required
def account_permission_update_post():
    return render_template(url_for('department.account_permissions'))

@permission.route('/account/permissions/delete', methods=['POST'])
@login_required
def account_permission_delete_post():
    return render_template(url_for('department.account_permissions'))