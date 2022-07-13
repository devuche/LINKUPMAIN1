from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json
import base64
from werkzeug.utils import secure_filename
from sqlalchemy import func
views = Blueprint('views', __name__)
@views.route('/')
def homepage():
    return render_template("Homepage.html")
@views.route('/second')
def second_page():
    return render_template("second.html")
@views.route('/third')
def third_page():
    return render_template("third.html")
@views.route('/signupone')
def signupone():
    return render_template("SignupEntrepreneur.html")
@views.route('/entrepreneur')
@login_required
def entrepreneur_one():
    return render_template("Entrepreneur.html")
@views.route('/entrepreneurtwo')
@login_required
def entrepreneur_two():
    return render_template("Entrepreneurtwo.html")
@views.route('/entrepreneurthree')
@login_required
def entrepreneur_three():
    return render_template("Entrepreneurthree.html")
def entrepreneur_four():
    return render_template("Entrepreneur.html")
@views.route('/logininfluencer')
def loginone():
    return render_template("Logininfluencer.html")
@views.route('/loginentrepreneur')
def logintwo():
    return render_template("Loginenterpreneur.html")


