# Making basic websites with Python

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Main Page</h1>"

@app.route('/<name>')
def user(name):
    return f"Hello, {name}!"

# Redirect to user function requires ('user', name='Admin') for the name parameter
@app.route('/admin')
def admin():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()