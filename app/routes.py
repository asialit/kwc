from flask import render_template, redirect, url_for, flash, request
from flask_login import current_user, login_user, logout_user

from app import app, db
from app.forms import LoginForm, AddCandidateForm
from app.models import User, Candidate


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        code = request.form["code"]
        candidate_id = request.form["candidate"]
        # code_exists = db.session.query(Vote.id).filter_by(code=code).first() is not None
    else:
        candidates = Candidate.query.all()
        return render_template('index.html', candidates=candidates)


# @login_required
@app.route('/admin')
def admin():
    # user = flask_login.current_user
    return render_template('admin.html')


@app.route('/admin/add_candidate', methods=['GET', 'POST'])
def add_candidate():
    form = AddCandidateForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        candidate = Candidate(name=name, surname=surname)
        db.session.add(candidate)
        db.session.commit()
        return redirect(url_for('admin'))
    return render_template('add_candidate.html', form=form)


@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/admin/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
