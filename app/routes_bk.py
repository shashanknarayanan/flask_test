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
    height="5 feet 6 inches"
    return render_template('test2.html', height=height)



