from flask import render_template, url_for, flash, redirect, jsonify, request
from FlaskLogin import app, db, bcrypt, basicLogger, auditLogger
from FlaskLogin.forms import RegistrationForm, LoginForm
from FlaskLogin.models import User
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    auditLogger.info("Received Data {} to URL: {}" .format(dict(request.form), request.url))
    data = {"Success ": "Responce"}
    return jsonify(data)

@app.route("/about")
def about():
    auditLogger.info("Received Data {} to URL: {}" .format(dict(request.form), request.url))
    return render_template('about.html', title="Tile Passing from File")

@app.route("/register", methods=['GET', 'POST'])
def register():
    print(dict(request.form))
    auditLogger.info("Received Data {} to URL: {}" .format(dict(request.form), request.url))
    if current_user.is_authenticated:
        basicLogger.info("user: {} alredy Logged In".format(current_user))
        auditLogger.info("user: {} alredy Logged In".format(current_user))
        return jsonify({"data": "user alredy Logged In"})
    form = RegistrationForm(request.form)
    if form:
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            basicLogger.exception(str(e))
            return jsonify({"data": "Failed to add the user", "Exception: ": str(e)})
        basicLogger.info("user created: {}".format(form.username.data))
        return jsonify({"data": "Your account has been created! You can now able to log in"})
    basicLogger.warning("Invalid Format Data Received: {}".format(dict(request.form)))
    return jsonify({"data": "Invalid Form"})

@app.route("/login", methods=['GET', 'POST'])
def login():
    print(dict(request.form))
    auditLogger.info("Received Data {} to URL: {}" .format(dict(request.form), request.url))
    if current_user.is_authenticated:
        basicLogger.info("user: {} alredy Logged In".format(current_user))
        auditLogger.info("user: {} alredy Logged In".format(current_user))
        return jsonify({"data": "user alredy Logged In " + str(current_user)})
    form = LoginForm()
    if form:
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            auditLogger.info("user - {} authenticated".format(user))
            return jsonify({"data": "authenticated successful"})
        else:
            return jsonify({"data: ": "Login Unsuccessful. Please check email and password"})
    return jsonify({"data": "Login Unsuccessful, Does user exists??"})

@app.route("/logout")
def logout():
    auditLogger.info("Received Data {} to URL: {}" .format(dict(request.form), request.url))
    logout_user()
    return jsonify({"data": "User Logged Out"})