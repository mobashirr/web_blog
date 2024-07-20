
# simple flask app:

from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == '__main__':
    app.run(debug=True) # run with the debug mode
