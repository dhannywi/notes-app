from flask import Blueprint, render_template

# define blueprint for application
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")