from rest_framework import serializers

from core.models import School, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'student_max_number')


class SchoolCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name', 'student_max_number')


class StudentSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'school', 'identification')


class StudentCreateSerializer(serializers.ModelSerializer):
    school_id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'school_id')


class SchoolUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('name', 'student_max_number')


class StudentUpdateSerializer(serializers.ModelSerializer):
    school_id = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'school_id')


class SchoolStudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name')
