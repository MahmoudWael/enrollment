import json
import unittest

from models import Enrollment
from models.abc import db
from repositories import EnrollmentRepository
from server import server


class TestEnroll(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        """ The GET on `/enroll` should return an enrollment """
        EnrollmentRepository.create(nanodegree_key="54848596", status="ENROLLED")
        response = self.client.get("/enroll/")
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        """ The POST on `/enroll` should create an enrollment """
        response = self.client.post(
            "enroll/",
            content_type="application/json",
            data=json.dumps({"nanodegree_key": "12345648", "status": "ENROLLED"}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Enrollment.query.count(), 1)

    def test_update(self):
        """ The PUT on `/enroll` should update an enrollment """
        enrollment = EnrollmentRepository.create(nanodegree_key="2432525", status="ENROLLED")
        response = self.client.put(
            "enroll/",
            content_type="application/json",
            data=json.dumps({"enrollment_id": enrollment.enrollment_id, "status": "UNENROLLED"}),
        )
        self.assertEqual(response.status_code, 200)
