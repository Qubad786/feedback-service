import os

from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

from app.server.db.extensions import db
from app.server.routes.page_not_found import page_not_found_blueprint
from app.server.routes.api_doc import api_doc_blueprint
from app.server.routes.index import reviews_blueprint

from app.server.api.api import AddReview, ListReviews, ExportReviews


def create_app(config_file):
    """
    Creating and returning the app
    """
    app_path = os.path.dirname(os.path.abspath(__file__))
    project_folder = os.path.expanduser(app_path)
    load_dotenv(os.path.join(project_folder, '.env'))

    app = Flask(__name__, template_folder='../client/templates', static_folder='../client/static')
    api = Api(app)
    app.config.from_pyfile(config_file)

    db.init_app(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

        api.add_resource(ListReviews, '/api/reviews/')
        api.add_resource(AddReview, '/api/reviews/add/')
        api.add_resource(ExportReviews, '/api/reviews/export/')

        app.register_blueprint(page_not_found_blueprint)
        app.register_blueprint(api_doc_blueprint)
        app.register_blueprint(reviews_blueprint)
        return app
