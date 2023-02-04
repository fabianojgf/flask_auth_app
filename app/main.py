from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
from . import db
from .models import User
from werkzeug.utils import secure_filename
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')