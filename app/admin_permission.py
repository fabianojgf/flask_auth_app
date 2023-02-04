from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_required, current_user
from datetime import datetime
from . import db
from .models import User, Permission, PermissionType, PermissionStatus, Department
import os

admin_permission = Blueprint('admin_permission', __name__)

@admin_permission.route('/admin/permissions')
@login_required
def permissions():
    nav_levels = ["Área Interna", "Admin", "Permissões"]

    permissions = Permission.query.filter_by(
        user_id=current_user.id, permission_type_id=3, active=True).all()
    permissions_sol = Permission.query.filter_by(
        user_id=current_user.id, permission_type_id=1, active=True).all()
    permissions_other = Permission.query.filter(
        Permission.user_id==current_user.id, Permission.permission_type_id>=2, Permission.active==True).all()

    # Selects
    permissionTypes = PermissionType.query.filter().all()
    departments = Department.query.filter().all()

    return render_template('admin/permissions/list.html', 
        permissions=permissions, 
        permissions_sol=permissions_sol, 
        permissions_other=permissions_other,
        permissionTypes=permissionTypes,
        departments=departments, 
        nav_levels=nav_levels)

@admin_permission.route('/admin/permissions/new')
@login_required
def permission_new():
    nav_levels = ["Área Interna", "Admin", "Permissões", "Novo"]

    # Selects
    permissionTypes = PermissionType.query.filter().all()
    departments = Department.query.filter().all()

    return render_template('admin/permissions/form-new.html',
        permissionTypes=permissionTypes,
        departments=departments, 
        nav_levels=nav_levels)

@admin_permission.route('/admin/permissions/new', methods=['POST'])
@login_required
def permission_new_post():
    return redirect(url_for('admin_permission.permissions'))

@admin_permission.route('/admin/permissions/edit')
@login_required
def permission_update():
    nav_levels = ["Área Interna", "Admin", "Permissões", "Editar"]
    return render_template('admin/permissions/form-edit.html', 
        nav_levels=nav_levels)

@admin_permission.route('/admin/permissions/edit', methods=['POST'])
@login_required
def permission_update_post():
    return redirect(url_for('admin_permission.permissions'))

@admin_permission.route('/admin/permissions/delete', methods=['POST'])
@login_required
def permission_delete_post():
    return redirect(url_for('admin_permission.permissions'))