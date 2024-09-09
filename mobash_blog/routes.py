
''' routes module '''


from mobash_blog.forms import RegistrationForm, loginForm
from mobash_blog.models import User, Post
from mobash_blog import app, db, encrypter
from flask import render_template, url_for,flash,redirect


data = [
    {
        'author': 'mohamed bashir',
        'title': 'Blog Post 1',
        'content': 'this is my First post ',
        'date_posted': 'JULY 20, 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'qoute',
        'content': 'the best way to master anything is to practice',
        'date_posted': 'JULY 21, 2024'
    },
    {
        'author': 'mohamed',
        'title': 'why flask?',
        'content': 'because flask is nice and simple',
        'date_posted': 'JULY 21, 2024'
    }
]


# the route is what you type in the url to get this web page
@app.route("/")
@app.route("/home")
def home():
    title = "HOME PAGE"
    posts = []
    for post in Post.query.all():
        posts.append(post.to_dict())
    return render_template('home.html', posts=posts, title=title)

@app.route("/about")
def about():
    title = "ABOUT PAGE"
    return render_template('about.html', title=title)

@app.route("/register", methods=['GET', 'POST'])
def register():
    '''registeration route'''
    title = 'registeraion'
    form = RegistrationForm()

    if form.validate_on_submit() and form.validate_username(form.username.data) and form.validate_email(form.email.data):
        pass_hashed = encrypter.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=pass_hashed)
        db.session.add(user)
        db.session.commit()
        flash(f"sign up for {form.username.data} has done seccessfully you can now login", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title=title, form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    '''log in route, the methods for route is to allow post data'''
    title = 'LOG IN'
    form = loginForm()
    if form.validate_on_submit() and form.validate_correct_info() is True: # is True for reason don't delete it
        flash(f"{form.email.data} seccessfully loged in", 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title=title, form=form)
