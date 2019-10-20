import logging
from typing import Union

from common.exceptions import ObjectNotFoundException, NotAcceptableException
from .models import School, Student

logger = logging.getLogger(__name__)


class SchoolService:
    model = School

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            logger.error('School with {params} does not exist'.format(
                params=', '.join(['{k}:{v}'.format(k=k, v=v) for k, v in filters.items()]))
            )
            raise ObjectNotFoundException('School not found')

    @classmethod
    def filter(cls, **filters):
        return cls.model.objects.filter(**filters)

    @classmethod
    def create(cls, name: str, student_max_number: int) -> School:
        return School.objects.create(name=name, student_max_number=student_max_number)

    @classmethod
    def is_max_students_number(cls, school: School):
        return school.students.count() == school.student_max_number

    @classmethod
    def update(cls, school: School, name: str, student_max_number: int) -> School:
        school.name = name
        school.student_max_number = student_max_number
        school.save()

        return school


class StudentService:
    model = Student

    @classmethod
    def get(cls, **filters):
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            logger.error('Student with {params} does not exist'.format(
                params=', '.join(['{k}:{v}'.format(k=k, v=v) for k, v in filters.items()]))
            )
            raise ObjectNotFoundException('School not found')

    @classmethod
    def filter(cls, **filters):
        return cls.model.objects.filter(**filters)

    @classmethod
    def create(cls, first_name: str, last_name: str, school: Union[School, None]) -> Student:

        if school:
            if SchoolService.is_max_students_number(school=school):
                raise NotAcceptableException(message='You can not add student to this school, school is full')

        return Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            school=school
        )

    @classmethod
    def update(cls, student: Student, school: Union[School, None], first_name: str, last_name: str) -> Student:
        if school:
            if SchoolService.is_max_students_number(school=school):
                raise NotAcceptableException(message='You can not add student to this school, school is full')

        student.school = school
        student.first_name = first_name
        student.last_name = last_name
        student.save()

        return student
