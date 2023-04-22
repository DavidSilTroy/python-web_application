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


    #initialize blueprints
    from webapp.blueprints.home.routes import home_views
    app.register_blueprint(home_views, url_prefix="/")


    return app