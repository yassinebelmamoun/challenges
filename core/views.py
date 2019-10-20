from rest_framework import status
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from common.constants import INVALID_INPUT
from common.responses import NotAcceptableExceptionResponse
from core.serializers import SchoolSerializer, SchoolCreateSerializer, StudentSerializer, StudentCreateSerializer, \
    SchoolUpdateSerializer, StudentUpdateSerializer, SchoolStudentCreateSerializer
from core.services import SchoolService, StudentService


class SchoolListCreateAPIView(ListCreateAPIView):
    queryset = SchoolService.filter()
    serializer_class = SchoolSerializer

    def create(self, request, *args, **kwargs):
        serializer = SchoolCreateSerializer(data=request.data, many=False)

        if not serializer.is_valid():
            return NotAcceptableExceptionResponse(data={'message': INVALID_INPUT, 'errors': serializer.errors})

        school = SchoolService.create(
            name=serializer.validated_data.get('name'),
            student_max_number=serializer.validated_data.get('student_max_number')
        )

        return Response(self.serializer_class(school).data, status=status.HTTP_201_CREATED)


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = StudentService.filter()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        serializer = StudentCreateSerializer(data=request.data, many=False)

        if not serializer.is_valid():
            return NotAcceptableExceptionResponse(data={'message': INVALID_INPUT, 'errors': serializer.errors})

        school = None

        if serializer.validated_data.get('school_id'):
            school = SchoolService.get(id=serializer.validated_data.get('school_id'))

        student = StudentService.create(
            first_name=serializer.validated_data.get('first_name'),
            last_name=serializer.validated_data.get('last_name'),
            school=school
        )

        return Response(data=self.serializer_class(student).data, status=status.HTTP_201_CREATED)


class SchoolUpdateView(APIView):
    def put(self, request, pk):
        serializer = SchoolUpdateSerializer(data=request.data, many=False)
        school = SchoolService.get(pk=pk)

        if not serializer.is_valid():
            return NotAcceptableExceptionResponse(data={'message': INVALID_INPUT, 'errors': serializer.errors})

        school = SchoolService.update(
            school=school,
            name=serializer.validated_data.get('name'),
            student_max_number=serializer.validated_data.get('student_max_number')
        )

        return Response(SchoolSerializer(school).data, status=status.HTTP_200_OK)


class StudentUpdateView(APIView):
    def put(self, request, pk):
        serializer = StudentUpdateSerializer(data=request.data, many=False)
        student = StudentService.get(pk=pk)

        if not serializer.is_valid():
            return NotAcceptableExceptionResponse(data={'message': INVALID_INPUT, 'errors': serializer.errors})

        school = None

        if serializer.validated_data.get('school_id'):
            school = SchoolService.get(id=serializer.validated_data.get('school_id'))

        student = StudentService.update(
            student=student,
            school=school,
            first_name=serializer.validated_data.get('first_name'),
            last_name=serializer.validated_data.get('last_name')
        )

        return Response(StudentSerializer(student).data, status=status.HTTP_200_OK)


class SchoolStudentsListView(ListCreateAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        school = SchoolService.get(pk=self.kwargs['pk'])
        return StudentService.filter(school=school)

    def create(self, request, *args, **kwargs):
        serializer = SchoolStudentCreateSerializer(data=request.data, many=False)

        school = SchoolService.get(pk=kwargs['pk'])
        student = StudentService.create(
            school=school,
            first_name=serializer.validated_data.get('first_name'),
            last_name=serializer.validated_data.get('last_name')
        )

        return Response(StudentSerializer(student).data, status=status.HTTP_200_OK)
