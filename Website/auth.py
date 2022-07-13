from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)

@auth.route('/loginentrepreneur', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.entrepreneur_one'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("Loginenterpreneur.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.homepage'))


@auth.route('/signupone', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('Email')
        name = request.form.get('Name')
        password1 = request.form.get('password')
        password2 = request.form.get('password2')
        category = request.form.get('category')
        categoryone = request.form.get('incategory')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 13:
            flash('Input valid email', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif category == '':
            flash('Choose a business category', category='error')
        elif categoryone == '':
            flash('Choose an Influencer category', category='error')
        else:
            new_user = User(email=email, name=name, business=category, influencer=categoryone, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.entrepreneur'))

    return render_template("SignupEntrepreneur.html", user=current_user)
