from models import Enrollment


class EnrollmentRepository:
    @staticmethod
    def get(udacity_user_key):
        """ Query enrollments by udacity_user_key """
        return Enrollment.query.filter_by(udacity_user_key=udacity_user_key).all()

    def _getById(self, enrollment_id):
        """ Query a single enrollments by enrollment_id """
        return Enrollment.query.filter_by(enrollment_id=enrollment_id).one()

    def update(self, enrollment_id, status):
        """ Update an enrollment """
        enrollment = self._getById(enrollment_id)
        enrollment.status = status

        return enrollment.save()

    @staticmethod
    def create(nanodegree_key, status):
        """ Create a new enrollment """
        enrollment = Enrollment(nanodegree_key=nanodegree_key, status=status)
        return enrollment.save()
