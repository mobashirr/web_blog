
# simple flask app:

from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm, loginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'b54af37ce9b4df9c42b12577ad7fd3fe'

data = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# the decorator route is what you type in the url to get this web page 
@app.route("/")
@app.route("/home")
def home():
    title = "HOME PAGE"
    return render_template('home.html', posts=data, title=title)

@app.route("/about")
def about():
    title = "ABOUT PAGEf"
    return render_template('about.html', title=title)

@app.route("/register", methods=['GET', 'POST'])
def register():
    '''registeration route'''
    title = 'registeraion'
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"sign up for {form.username.data} has done seccessfully", 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title=title, form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    '''log in route, the methods for route is to allow post data'''
    title = 'LOG IN'
    form = loginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f"log in to {form.email.data} has done seccessfully", 'success')
            return redirect(url_for('home'))
        else:
             flash(f"your email or password isn't correct", 'danger')

    return render_template('login.html', title=title, form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) # run with the debug mode
