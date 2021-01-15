from flask import request
from app import app 
import os

@app.route("/")
def index():
    '''
    The index route will demo how to use environment variables to generate
    dynamic responses from the API
    
    Try running the app without the variable
    and then set this variable and see how it changes:
    
        export APP_NAME=YOU_CHOOSE_A_NAME
    
    '''
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"

@app.route("/users/<username>", )
def display_user(username):
    '''
    Demos a way to handle args from the client
    '''

    return f"The user is: {username}"


@app.route("/puppies", methods=['GET', 'POST'] )
def puppies():
    '''
    This method demos the more sound way to handle args in requests
    Good to read : https://hackersandslackers.com/flask-routes/
    '''
    
    if request.method == 'GET':
        return f"There are no registered puppies"
    elif request.method == 'POST':
        puppy_name = request.form.get('puppy_name')
        return f"My puppies is: {puppy_name}"




