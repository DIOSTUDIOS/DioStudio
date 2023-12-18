from flask import Blueprint, render_template, redirect, url_for, request, flash
from application.models import db, Favorite
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class FavoritesAdd(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '网站名称'})
    cLink = StringField(label='cLink',
                        validators=[DataRequired(), ],
                        render_kw={'class_': 'full-width', 'placeholder': '网站地址'})
    cSummary = TextAreaField(label='cSummary',
                             validators=[DataRequired(), ],
                             render_kw={'class_': 'full-width','placeholder': '网站简介 ...'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '添加'})


class FavoritesDelete(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '网站名称'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '删除'})


favoritesPage = Blueprint('favoritesPage', __name__)


@favoritesPage.route('/favorites')
def favorites():
    favorites_list = db.session.query(Favorite.title, Favorite.link, Favorite.summary).order_by(Favorite.title).all()

    return render_template('page/favorites.html', favorites=favorites_list)


@favoritesPage.route('/favorites/add', methods=['GET', 'POST'])
def favorites_add():
    form = FavoritesAdd()
    if request.method == 'POST':
        if form.validate_on_submit():
            favorite = Favorite(title=form.cTitle.data,
                                link=form.cLink.data,
                                summary=form.cSummary.data)

            db.session.add(favorite)
            db.session.commit()

            return redirect(url_for('favoritesPage.favorites'))

    return render_template('page/favorites_add.html', form=form)


@favoritesPage.route('/favorites/delete', methods=['GET', 'POST'])
def favorites_delete():
    favorites_list = db.session.query(Favorite.title, Favorite.link, Favorite.summary).order_by(Favorite.title).all()
    form = FavoritesDelete()

    if request.method == 'POST':
        if form.validate_on_submit():
            favorite = Favorite.query.filter_by(title=form.cTitle.data).first()

            db.session.delete(favorite)
            db.session.commit()

            return redirect(url_for('favoritesPage.favorites'))

    return render_template('page/favorites_delete.html', favorites=favorites_list, form=form)


@favoritesPage.route('/favorites/edit/')
def favorites_edit():
    pass
