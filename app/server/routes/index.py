from flask import render_template, Blueprint

reviews_blueprint = Blueprint('reviews', 'reviews', template_folder='templates')


@reviews_blueprint.route("/")
def reviews():
    return render_template('reviews.html')
