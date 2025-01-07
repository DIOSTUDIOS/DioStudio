from flask import Blueprint, render_template


aboutPage = Blueprint('aboutPage', __name__)


@aboutPage.route('/about')
def about():
    return render_template('about/about.html')
