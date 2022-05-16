from urllib.parse import urlparse

from flask_restful import reqparse


def url_validator(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except TypeError:
        return False


add_review_parser = reqparse.RequestParser(bundle_errors=True)
list_reviews_parser = reqparse.RequestParser(bundle_errors=True)

add_review_parser.add_argument('url', type=str, help='URL parameter is missing', required=True)
add_review_parser.add_argument('review', type=str, help='Review is missing', required=True)

list_reviews_parser.add_argument('start', type=int, help='Page number in pagination', default=1, location='args')
list_reviews_parser.add_argument('length', type=int, help='Reviews per page', default=1, location='args')
