from . import db
from .abc import BaseModel, MetaBaseModel
import uuid
import datetime


class Enrollment(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The enrollment model """

    __tablename__ = "enrollment"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    enrollment_id = db.Column(db.String(300))
    nanodegree_key = db.Column(db.String(300), nullable=False)
    udacity_user_key = db.Column(db.Integer, nullable=True)
    enrolled_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    status = db.Column(db.String(300), nullable=False)

    def __init__(self, nanodegree_key, status):
        self.enrollment_id = uuid.uuid1().int
        self.nanodegree_key = nanodegree_key
        self.udacity_user_key = "1111"
        self.status = status

    def __iter__(self):
        return self.to_dict().iteritems()
