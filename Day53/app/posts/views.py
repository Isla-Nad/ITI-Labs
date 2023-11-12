from datetime import datetime
from flask import current_app, request, render_template, redirect, send_from_directory, url_for, flash
from app.models import Post, Category,  db
from app.posts import post_blueprint
from werkzeug.utils import secure_filename
import os

# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# def allowed_file(filename):
# 	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@post_blueprint.route('/', endpoint='posts_list')
def posts_list():
    posts = Post.get_all_posts()
    return render_template('posts/index.html', posts=posts)


@post_blueprint.route('/contact')
def contact_us():
    return render_template('contacts/contact_us.html')


@post_blueprint.route('/about')
def about_us():
    return render_template('contacts/about_us.html')


@post_blueprint.route('/details/<int:id>', endpoint='post_details')
def post_details(id):
    post = Post.query.get_or_404(id)
    return render_template('posts/post_details.html', post=post)


@post_blueprint.route('/create', endpoint='post_create', methods=['GET', 'POST'])
def create_post():
    categories = Category.get_all_categories()

    if 'title' in request.form and 'body' in request.form and 'image' in request.files and 'category' in request.form:
        title = request.form['title']
        body = request.form['body']
        image = request.files['image']
        category_id = request.form['category']

        if not title or not body or not category_id:
            return render_template('posts/create_post.html', error='Title, category and body are required fields')

        if image.filename == '':
            return render_template('posts/create_post.html', error='No selected image')

        if image:
            filename = secure_filename(image.filename)
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.{filename}"
            image_path = os.path.join(
                current_app.config["UPLOADED_PHOTOS_DEST"], filename)
            image.save(image_path)

            # filename = secure_filename(image.filename)
            # image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            # image.save(image_path)

            new_post = Post(title=title, body=body,
                            image=filename, category_id=category_id, created_at=datetime.utcnow())
            db.session.add(new_post)
            db.session.commit()

            return redirect(url_for('posts.posts_list'))
        else:
            return render_template('posts/create_post.html', categories=categories, error='Image file type not allowed')

    return render_template('posts/create_post.html', categories=categories, error='Title, body, category and image are required fields')


@post_blueprint.route('/uploads/<filename>')
def send_uploaded_file(filename):
    return send_from_directory(current_app.config["UPLOADED_PHOTOS_DEST"], filename)

# @post_blueprint.route('/display/<filename>')
# def display_image(filename):
# 	return redirect(url_for('static', filename='uploads/' + filename), code=301)


@post_blueprint.route('/edit/<int:id>', endpoint='post_edit', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    categories = Category.get_all_categories()

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        image = request.files['image']
        category_id = request.form['category']

        if not title or not body:
            flash('Title and body are required fields', 'error')
        else:
            post.title = title
            post.body = body
            post.category_id = category_id
            if image:
                os.remove(
                    current_app.config["UPLOADED_PHOTOS_DEST"]+'/'+post.image)
                filename = secure_filename(image.filename)
                image.save(os.path.join(
                    current_app.config["UPLOADED_PHOTOS_DEST"], filename))
                post.image = filename

            db.session.commit()
            flash('Post updated successfully', 'success')
            return redirect(url_for('posts.post_details', id=post.id))

    return render_template('posts/edit_post.html', categories=categories, post=post)


@post_blueprint.route('/delete/<int:id>', endpoint='post_delete', methods=['GET', 'POST'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        if post.image:
            os.remove(
                current_app.config["UPLOADED_PHOTOS_DEST"]+'/'+post.image)

        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('posts.posts_list'))
    return render_template('posts/delete_post.html', post=post)
