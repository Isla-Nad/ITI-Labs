from datetime import datetime
from flask import current_app, request, render_template, redirect, url_for, flash
from app.categories import category_blueprint
from app.models import Category, db
from werkzeug.utils import secure_filename
import os


@category_blueprint.route('/', endpoint='categories_list')
def categories_list():
    categories = Category.get_all_categories()
    return render_template('categories/list.html', categories=categories)


@category_blueprint.route('/<int:id>', endpoint='category_details')
def category_details(id):
    category = Category.get_specific_category(id)
    return render_template('categories/details.html', category=category)


@category_blueprint.route('/create', endpoint='category_create', methods=['GET', 'POST'])
def create_category():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image = request.files['image']

        if not name:
            return render_template('categories/create.html', error='Name is a required field')

        if image.filename == '':
            return render_template('categories/create.html', error='No selected image')

        if image:
            filename = secure_filename(image.filename)
            filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}.{filename}"
            image_path = os.path.join(
                current_app.config["UPLOADED_PHOTOS_DEST"], filename)
            image.save(image_path)

            new_category = Category(
                name=name, description=description, image=filename)
            db.session.add(new_category)
            db.session.commit()

            return redirect(url_for('category.categories_list'))

    return render_template('categories/create.html', error=None)


@category_blueprint.route('/<int:id>/edit', endpoint='category_edit', methods=['GET', 'POST'])
def edit_category(id):
    category = Category.get_specific_category(id)

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image = request.files['image']

        if not name:
            flash('Name is a required field', 'error')
        else:
            category.name = name
            category.description = description
            if image:
                os.remove(os.path.join(
                    current_app.config["UPLOADED_PHOTOS_DEST"], category.image))
                filename = secure_filename(image.filename)
                image.save(os.path.join(
                    current_app.config["UPLOADED_PHOTOS_DEST"], filename))
                category.image = filename

            db.session.commit()
            flash('Category updated successfully', 'success')
            return redirect(url_for('category.category_details', id=category.id))

    return render_template('categories/edit.html', category=category)


@category_blueprint.route('/<int:id>/delete', endpoint='category_delete', methods=['GET', 'POST'])
def delete_category(id):
    category = Category.get_specific_category(id)
    if request.method == 'POST':
        if category.image:
            os.remove(os.path.join(
                current_app.config["UPLOADED_PHOTOS_DEST"], category.image))

        db.session.delete(category)
        db.session.commit()
        return redirect(url_for('category.categories_list'))
    return render_template('categories/delete.html', category=category)
