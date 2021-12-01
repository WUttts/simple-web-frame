from flask import Blueprint,render_template,request
from src.service.test_service import TestService

page = Blueprint("page", __name__, url_prefix='')

@page.route('/')
def index():
    return render_template("index.html")