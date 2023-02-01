from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db
from .models import User, Access, PermissionType, PermissionStatus, Permission, Department
import os

account_permission = Blueprint('account_permission', __name__)

@account_permission.route('/account/permissions')
@login_required
def permissions():
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

@account_permission.route('/account/permissions/new')
@login_required
def permission_new():

    # Selects
    permissionTypes = PermissionType.query.filter().all()
    departments = Department.query.filter().all()

    return render_template('account/permissions/form-new.html',
        permissionTypes=permissionTypes,
        departments=departments)

@account_permission.route('/account/permissions/new', methods=['POST'])
@login_required
def permission_new_post():
    return render_template(url_for('account_permission.permissions'))

@account_permission.route('/account/permissions/edit')
@login_required
def permission_update():
    return render_template('account/permissions/form-edit.html')

@account_permission.route('/account/permissions/edit', methods=['POST'])
@login_required
def permission_update_post():
    return render_template(url_for('account_permission.permissions'))

@account_permission.route('/account/permissions/delete', methods=['POST'])
@login_required
def permission_delete_post():
    return render_template(url_for('account_permission.permissions'))