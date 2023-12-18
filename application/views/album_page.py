from flask import Blueprint, render_template, request, redirect, url_for
from application.models import db, Album
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


albumPage = Blueprint('albumPage', __name__)


class AlbumAdd(FlaskForm):
    cTitle = StringField(label='cTitle',
                         validators=[DataRequired(), ],
                         render_kw={'class_': 'full-width', 'placeholder': '专辑名称'})
    cSummary = TextAreaField(label='cSummary',
                             validators=[DataRequired(), ],
                             render_kw={'class_': 'full-width','placeholder': '专辑简介 ...'})
    cSubmit = SubmitField(label='cSubmit',
                          render_kw={'class_': 'btn button-primary full-width-on-mobile', 'value': '添加'})

    pass


@albumPage.route('/albums')
def albums():
    paginate = Album.query.paginate(per_page=8, error_out=False)

    return render_template('page/albums.html', albums=paginate.items, paginate=paginate)


@albumPage.route('/albums/add', methods=['GET', 'POST'])
def albums_add():
    form = AlbumAdd()

    if request.method == 'POST':
        if form.validate_on_submit():
            album = Album(title=form.cTitle.data,
                          summary=form.cSummary.data)

            db.session.add(album)
            db.session.commit()

            return redirect(url_for('albumPage.albums'))

    return render_template('page/albums_add.html', form=form)
    pass


@albumPage.route('/albums/delete')
def albums_delete():
    pass
