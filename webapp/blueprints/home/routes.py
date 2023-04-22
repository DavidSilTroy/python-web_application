from webapp.blueprints.home import home_views
from flask import render_template

@home_views.route('')
@home_views.route('/')
@home_views.route('/index')
@home_views.route('/home')
def home():
    return render_template("pages/home/index.html") 