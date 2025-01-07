from flask import Blueprint, render_template


pageNotFound = Blueprint('pageNotFound', __name__, template_folder='templates', static_folder='static')


@pageNotFound.app_errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404
