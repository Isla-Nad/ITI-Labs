from flask_uploads import IMAGES, UploadSet, configure_uploads
from flask import flash, redirect, render_template, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = 'media/images'
app.config["SECRET_KEY"] = os.urandom(24)
configure_uploads(app, photos)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @classmethod
    def get_all_posts(cls):
        return cls.query.all()

    @classmethod
    def get_specific_post(cls, id):
        return cls.query.get_or_404(id)


@app.route('/', endpoint='posts.list')
def posts_list():
    posts = Post.get_all_posts()
    return render_template('posts/index.html', posts=posts)


@app.route('/contact')
def contact_us():
    return render_template('contacts/contact_us.html')


@app.route('/about')
def about_us():
    return render_template('contacts/about_us.html')


@app.route('/details/<int:id>', endpoint='post.details')
def post_details(id):
    post = Post.query.get_or_404(id)
    return render_template('posts/post_details.html', post=post)


@app.route('/create', endpoint='post.create', methods=['GET', 'POST'])
def create_post():
    if 'title' in request.form and 'body' in request.form and 'image' in request.files:
        title = request.form['title']
        body = request.form['body']
        image = request.files['image']

        if not title or not body:
            return render_template('posts/create_post.html', error='Title and body are required fields')

        if image.filename == '':
            return render_template('posts/create_post.html', error='No selected image')

        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(
                app.config["UPLOADED_PHOTOS_DEST"], filename)
            image.save(image_path)
            new_post = Post(title=title, body=body,
                            image=filename, created_at=datetime.utcnow())
            db.session.add(new_post)
            db.session.commit()

            return redirect(url_for('posts.list'))
        else:
            return render_template('posts/create_post.html', error='Image file type not allowed')

    return render_template('posts/create_post.html', error='Title, body, and image are required fields')


@app.route('/uploads/<filename>')
def send_uploaded_file(filename):
    return send_from_directory(app.config["UPLOADED_PHOTOS_DEST"], filename)


@app.route('/edit/<int:id>', endpoint='post.edit', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        image = request.files['image']

        if not title or not body:
            flash('Title and body are required fields', 'error')
        else:
            post.title = title
            post.body = body
            if image:
                os.remove(app.config["UPLOADED_PHOTOS_DEST"]+'/'+post.image)
                filename = secure_filename(image.filename)
                image.save(os.path.join(
                    app.config['UPLOADED_PHOTOS_DEST'], filename))
                post.image = filename

            db.session.commit()
            flash('Post updated successfully', 'success')
            return redirect(url_for('post.details', id=post.id))

    return render_template('posts/edit_post.html', post=post)


@app.route('/delete/<int:id>', endpoint='post.delete', methods=['GET', 'POST'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        if post.image:
            os.remove(app.config["UPLOADED_PHOTOS_DEST"]+'/'+post.image)

        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('posts.list'))
    return render_template('posts/delete_post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
