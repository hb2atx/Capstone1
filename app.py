# from werkzeug.exception import Unauthorized
import os
import requests
from flask import Flask, render_template,redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import RegisterForm, LoginForm
from models import db, connect_db, User
from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.app_context().push()
bcrypt = Bcrypt(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///nfl.db'
app.config['SECRET_KEY'] = 'mysecretkey'
app.config["SQLALCHEMY_ECHO"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)


toolbar = DebugToolbarExtension(app)


    
@app.route('/')
def home():

    # Homepage wih links to site areas


    return render_template('home.html')

@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():

    return render_template('/dashboard.html')


@app.route('/register', methods=["GET", "POST"])
def register_user():
    form = RegisterForm()
    if form.validate_on_submit():
      username = form.username.data
      password = form.password.data
      new_user = User.register(username, password)

      db.session.add(new_user)
      try:
          db.session.commit()
      except IntegrityError:
          form.username.errors.append('Username taken. Please pick another')
          return render_template('register.html', form=form)
      session['user_id'] = new_user.id
      flash('Welcome! Successfully created your account!', "success")
      return redirect('/login')
    
    return render_template('register.html', form=form)

 
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
      username = form.username.data
      password = form.password.data

      user = User.authenticate(username, password)
      if user:
          flash(f"Welcome Back, {user.username}!", "primary")
          session["user_id"] = user.id
          return redirect('/dashboard')
      else:
          form.username.errors = ['Ivalid Usename/Password']

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_user():
    session.pop('user_id')
    flash("Goodbye!", "info")
    return redirect('/')








  
  


      




