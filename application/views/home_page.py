from flask import Blueprint, render_template


homePage = Blueprint('homePage', __name__)


@homePage.route('/')
def index():
    return render_template('index.html')
