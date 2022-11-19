from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
    return """
    <html>
        <head>
            <title> Home </title>
        </head>
        <body>
            <div><a href ="/about"> About </a></div>
            <div><a href ="/test"> Test Page <a></div>
            <div><a href ="/test2"> Test2 Page <a></div>
            <div><a href ="/homework"> Homework Page <a></div>
        </body>
    </html>
    
    """

@app.route('/about')
def about():
    return "About"

@app.route('/test')
def test():
    user = {'username': 'Shashank'}
    age=20
    return render_template('test.html', user=user, age=age)
@app.route('/test2')
def test2():
    user = {'username': 'Seb'}
    sample_data = [
    {
    'author': {'username': 'Seb'},
    'body': 'Hello!'
    },
    {
    'author': {'username': 'Shashank'},
    'body': 'Welcome to Flask!'
    }
    ]
    return render_template('test2.html', user=user, sample_data=sample_data)

@app.route('/homework')
def homework():
    amount=27
    return render_template('homework.html', amount=amount)