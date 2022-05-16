import os
import requests
from flask import send_file
from flask_restful import Resource
from werkzeug.exceptions import NotFound

from app.server.api.api_auth import auth
from app.server.db.models import Review
from .parsers import add_review_parser, list_reviews_parser


class AddReview(Resource):
    """
    Add a new review to UI
    URL: /api/reviews/add/
    METHOD: POST
    PARAMS: url: URL, review: String
    HEADERS: Authorization: (Bearer <key>)
    RETURN: Created review id
    """

    decorators = [auth.login_required]

    @staticmethod
    def post():
        args = add_review_parser.parse_args()
        url = args['url']
        review = args['review']

        try:
            review = Review.add_review(url, review)
            return dict(
                review_id=review.id,
                success=True
            ), 201

        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            return dict(
                success=False,
                message='Could not save review (page_not_found)'
            ), 503


class ListReviews(Resource):
    """
    Get paginated reviews
    URL: /api/reviews/
    METHOD: POST
    PARAMS: start: int, end: int, limit: int
    HEADERS: Authorization: (Bearer <key>)
    RETURN: list of reviews
    """

    @staticmethod
    def get():
        args = list_reviews_parser.parse_args()
        page_no = args['start']
        per_page = args['length']

        try:
            reviews = Review.query.paginate(page=page_no, per_page=per_page).items
            return dict(
                draw=1,
                recordsTotal=Review.query.count(),
                recordsFiltered=len(reviews),
                data=[r.as_dict() for r in reviews]
            ), 200

        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            return dict(
                success=False,
                message='Could not save review (page_not_found)'
            ), 503
        except NotFound:
            return [], 400


class ExportReviews(Resource):
    """
    Get reviews csv
    URL: /api/reviews/export/
    METHOD: POST
    HEADERS: Authorization: (Bearer <key>)
    RETURN: csv containing reviews
    """

    @staticmethod
    def get():
        try:
            reviews = Review.query.all()
            file_basename = create_csv(reviews)

            return send_file(
                file_basename,
                mimetype="text/csv",
                attachment_filename=file_basename,
            )

        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            return dict(
                success=False,
                message='Could not save review (page_not_found)'
            ), 503
        except NotFound:
            return [], 400


def create_csv(data):
    """
    returns (file_basename, server_path, file_size)
    """
    server_path = os.path.abspath('')
    file_path = os.path.join(server_path, 'reviews.csv')
    w_file = open(file_path, 'w')
    w_file.write('Id,Url,Date Created,Review\n')

    w_file.write(''.join([
        ','.join(list(d.as_dict().values())) + '\n'
        for d in data
    ]))

    w_file.close()
    return file_path
