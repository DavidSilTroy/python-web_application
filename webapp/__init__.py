from flask import Flask, redirect, url_for

from config import Config

#run the app once the script is running
def create_app(): 
    #configuring web-app with ist name and folders
    app = Flask(
    "Web Application" ,
    static_folder='webapp/static',
    template_folder='webapp/templates'
    )
    #setting web-app configuration
    app.config.from_object(Config)


    @app.route('/')
    @app.route('/index')
    @app.route('/home')
    def home():
        return "hello world! :)" 


    return app