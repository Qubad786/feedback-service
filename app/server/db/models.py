from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import ForeignKey

from .extensions import db
from .utils import get_one_or_create


@dataclass
class TrueNASURL(db.Model):
    id: int
    url: str

    __tablename__ = 'ui_url'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(512))
    date_created = db.Column(db.DateTime, default=datetime.now)
    reviews = db.relationship('Review', back_populates='url')

    def __repr__(self):
        return self.url


@dataclass
class Review(db.Model):
    id: int
    url: str
    date_created: datetime
    review: str

    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, ForeignKey('ui_url.id'))
    url = db.relationship('TrueNASURL', back_populates='reviews')
    review = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.now)

    @staticmethod
    def add_review(url, review):
        url, _ = get_one_or_create(db.session, TrueNASURL, url=url)
        review = Review(url_id=url.id, review=review)
        db.session.add(review)
        db.session.commit()

        return review

    def as_dict(self):
        # TODO: Find some better way to serialize foreign keys
        return {c: str(getattr(self, c)) for c in self.__annotations__.keys()}
