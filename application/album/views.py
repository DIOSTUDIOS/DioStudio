from flask import Blueprint, render_template, request, redirect, url_for
from application.plugin import db
from application.album.model import Album
from application.album.forms import AddAlbum, DelAlbum


albumPage = Blueprint('albumPage', __name__)


@albumPage.route('/albums')
def get_albums():
    paginate = Album.query.paginate(per_page=8, error_out=False)

    return render_template('album/albums.html', albums=paginate.items, paginate=paginate)


@albumPage.route('/albums/add', methods=['GET', 'POST'])
def add_album():
    form = AddAlbum()

    if request.method == 'POST':
        if form.validate_on_submit():
            album = Album(title=form.cTitle.data,
                          summary=form.cSummary.data)

            db.session.add(album)
            db.session.commit()

            return redirect(url_for('albumPage.get_albums'))

    return render_template('album/album_add.html', form=form)
    pass


@albumPage.route('/albums/delete', methods=['GET', 'POST'])
def del_album():
    album_list = Album.query.all()
    form = DelAlbum()

    if request.method == 'POST':
        if form.validate_on_submit():
            album = Album.query.filter_by(title=form.cTitle.data).first()

            db.session.delete(album)
            db.session.commit()

        return redirect(url_for('albumPage.get_albums'))

    return render_template('album/album_delete.html', form=form, albums=album_list)
    pass
