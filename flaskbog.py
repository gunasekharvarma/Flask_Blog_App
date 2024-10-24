from flask import Flask
from flask import render_template

app = Flask(__name__)

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
def hello_world():
    return render_template('about.html',title='About')


if __name__ == "__main__":
    app.run(debug=True)