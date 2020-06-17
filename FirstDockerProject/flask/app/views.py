from app import app
import os

@app.route('/')
def index():

    app_name = os.getenv('APP_NAME')

    if app_name:
        return "Hello from {} running in a Docker container behind Nginx".format(app_name)

    return "Hello from Flask"
