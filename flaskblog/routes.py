from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [

    {
        'author' : 'Guna Sekhar Varma',
        'title' : 'My First Blog Post 1',
        'content' : 'I started building my profile by doing projects',
        'date_posted' : 'Oct 24, 2024'
    },
    {
        'author' : 'Hari Krishna Reddy',
        'title' : 'My First Blog Post 1',
        'content' : 'I have Mphasis Interview tomorrow',
        'date_posted' : 'Oct 24, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET','POST'])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!",'success')
        return redirect(url_for('home_page'))
    return render_template('register.html',title='Register',form=form)

@app.route("/login", methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "guna@gmail.com" and form.password.data == "password":
            flash('You have sucessfully logged In', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Login is Unsuccessful, Please check username and password', 'danger')
    return render_template('login.html',title='Login',form=form)
