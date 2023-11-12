from flask_restful import Resource, marshal_with
from app.models import Post, db
from app.posts.api.serializers import post_serializer
from flask import abort, make_response, request
from app.posts.api.parsers import post_request_parser


class PostListClass(Resource):
    @marshal_with(post_serializer)
    def get(self):
        posts = Post.get_all_posts()
        return posts

    @marshal_with(post_serializer)
    def post(self):
        post_args = post_request_parser.parse_args()
        post = Post.save_object(post_args)
        return post, 201


class PostResource(Resource):
    @marshal_with(post_serializer)
    def get(self, post_id):
        post = Post.get_specific_post(post_id)
        return post, 200

    @marshal_with(post_serializer)
    def put(self, post_id):
        post = Post.get_specific_post(post_id)
        if post:
            std_args = post_request_parser.parse_args()
            post.title = std_args['title']
            post.body = std_args['body']
            post.image = std_args['image']
            post.category_id = std_args['category_id']
            db.session.add(post)
            db.session.commit()

            return post, 200

        abort(404, message='Student object not found')

    def delete(self, post_id):
        post = Post.get_specific_post(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            response = make_response("deleted", 204)
            return response

        abort(404)
