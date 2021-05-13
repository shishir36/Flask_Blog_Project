from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'Shishir Hossain',
        'title' : 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted' : 'May 10, 2021'

    },
    {
        'author' : 'Max Plank',
        'title' : 'Blog Post 2',
        'content' : 'Second Post content',
        'date_posted' : 'May 15, 2021'

    } 

]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/ajaira')
def ajaira():
    return "<h1> !! Ajaira Page !!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
