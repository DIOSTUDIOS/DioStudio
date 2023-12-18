from flask import Blueprint, render_template


discussPage = Blueprint('discussPage', __name__)


@discussPage.route('/discuss')
def discuss():
    return render_template('page/discuss.html')
