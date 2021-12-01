from flask import Blueprint,render_template

page = Blueprint("page", __name__, url_prefix='')

@page.route('/')
def index():
    return render_template("index.html")