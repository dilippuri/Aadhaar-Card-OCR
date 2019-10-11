from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Dilip Puri',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template('home.html', posts=posts, title='DocOcr')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
