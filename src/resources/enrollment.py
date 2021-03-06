from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask import request

from repositories import EnrollmentRepository


class EnrollmentResource(Resource):
    @staticmethod
    @swag_from("../swagger/enrollment/GET.yml")
    def get():
        # udacity_user_key = request.args.get('udacity_user_key')
        udacity_user_key = "1111"   # dummy_key is set to 1111
        enrollment = EnrollmentRepository.get(udacity_user_key=udacity_user_key)
        return jsonify({'enrollment': [row.json for row in enrollment]})

    @staticmethod
    @swag_from("../swagger/enrollment/POST.yml")
    def post():
        parameters = request.json
        nanodegree_key = parameters.get('nanodegree_key')
        status = parameters.get('status')
        enrollment = EnrollmentRepository.create(
            nanodegree_key=nanodegree_key, status=status
        )
        return jsonify({"enrollment": enrollment.json})

    @staticmethod
    @swag_from("../swagger/enrollment/PUT.yml")
    def put():
        parameters = request.json
        enrollment_id = parameters.get('enrollment_id')
        status = parameters.get('status')
        repository = EnrollmentRepository()
        enrollment = repository.update(enrollment_id=enrollment_id, status=status)
        return jsonify({"enrollment": enrollment.json})
