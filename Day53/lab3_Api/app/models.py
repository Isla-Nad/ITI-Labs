
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_onupdate=db.func.now(), server_default=db.func.now())
    posts = db.relationship('Post', backref='category_name',
                            lazy=True, cascade='all, delete-orphan')

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_categories(cls):
        return cls.query.all()

    @classmethod
    def get_specific_category(cls, id):
        return cls.query.get_or_404(id)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    image = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_onupdate=db.func.now(), server_default=db.func.now())
    category_id = db.Column(db.Integer, db.ForeignKey(
        'categories.id'), nullable=False)
    category = db.relationship('Category', backref='post_title')

    def __str__(self):
        return f"{self.title}"

    @classmethod
    def get_all_posts(cls):
        return cls.query.all()

    @classmethod
    def get_specific_post(cls, id):
        return cls.query.get_or_404(id)

    @classmethod
    def save_object(cls, requestdata):
        post = cls(**requestdata)
        db.session.add(post)
        db.session.commit()
        return post
