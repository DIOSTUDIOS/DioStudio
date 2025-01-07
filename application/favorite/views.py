from flask import Blueprint, render_template, redirect, url_for, request
from application.plugin import db
from application.favorite.model import Favorite
from application.favorite.forms import AddFavorite, DelFavorite


favoritesPage = Blueprint('favoritesPage', __name__)

@favoritesPage.route('/favorites')
def get_favorites():
    favorites_list = db.session.query(Favorite.title, Favorite.link, Favorite.summary).order_by(Favorite.title).all()

    return render_template('favorite/favorites.html', favorites=favorites_list)


@favoritesPage.route('/favorites/add', methods=['GET', 'POST'])
def add_favorite():
    form = AddFavorite()

    if request.method == 'POST':
        if form.validate_on_submit():
            favorite = Favorite(title=form.cTitle.data,
                                link=form.cLink.data,
                                summary=form.cSummary.data)

            db.session.add(favorite)
            db.session.commit()

            return redirect(url_for('favoritesPage.favorites'))

    return render_template('favorite/favorites_add.html', form=form)


@favoritesPage.route('/favorites/delete', methods=['GET', 'POST'])
def delete_favorite():
    form = DelFavorite()
    favorites_list = db.session.query(Favorite.title, Favorite.link, Favorite.summary).order_by(Favorite.title).all()

    if request.method == 'POST':
        if form.validate_on_submit():
            favorite = Favorite.query.filter_by(title=form.cTitle.data).first()

            db.session.delete(favorite)
            db.session.commit()

            return redirect(url_for('favoritesPage.favorites'))

    return render_template('favorite/favorites_delete.html', favorites=favorites_list, form=form)


@favoritesPage.route('/favorites/edit/')
def edit_favorite():
    pass
