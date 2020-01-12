"""
Defines the blueprint for the enrollments
"""
from flask import Blueprint
from flask_restful import Api

from resources import EnrollmentResource

ENROLLMENT_BLUEPRINT = Blueprint("enrollment", __name__)
Api(ENROLLMENT_BLUEPRINT).add_resource(
    EnrollmentResource, "enroll/"
)
