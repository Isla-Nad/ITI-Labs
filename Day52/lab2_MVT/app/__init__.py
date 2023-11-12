from flask import Flask
from flask_migrate import Migrate
from flask_uploads import IMAGES, UploadSet, configure_uploads
from app.models import db
from app.config import projectConfig as AppConfig
import os


def create_app(config_name='dev'):
    UPLOAD_FOLDER = 'static/uploads/'

    app = Flask(__name__)
    current_config = AppConfig[config_name]
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config.from_object(current_config)

    photos = UploadSet("photos", IMAGES)
    app.config["UPLOADED_PHOTOS_DEST"] = 'media/images'
    app.config["SECRET_KEY"] = os.urandom(24)
    configure_uploads(app, photos)

    # app.secret_key = os.urandom(24)
    # app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    # app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    db.init_app(app)

    migrate = Migrate(app, db, render_as_batch=True)

    from app.posts import post_blueprint
    app.register_blueprint(post_blueprint)

    from app.categories import category_blueprint
    app.register_blueprint(category_blueprint)

    return app
