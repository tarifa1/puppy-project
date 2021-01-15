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
    https://hackersandslackers.com/flask-routes/
    '''

    return f"The user is: {username}"




