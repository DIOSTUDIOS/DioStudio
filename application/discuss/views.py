from flask import Blueprint, render_template


discussPage = Blueprint('discussPage', __name__)


@discussPage.route('/discuss')
def get_discussions():
    return render_template('discuss/discuss.html')

@discussPage.route('/discuss/add')
def add_discussion():
    pass

@discussPage.route('/discuss/delete')
def del_discussion():
    pass
