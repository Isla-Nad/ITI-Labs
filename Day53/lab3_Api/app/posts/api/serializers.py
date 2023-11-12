from flask_restful import fields

category_serlizer = {
    "id": fields.Integer,
    "name": fields.String,
    "description": fields.String,
    "image": fields.String
}
post_serializer = {
    "id": fields.Integer,
    'title': fields.String,
    'body': fields.String,
    'image': fields.String,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime,
    "category_id": fields.Integer,
    'category_name': fields.Nested(category_serlizer)
}
