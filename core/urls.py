from django.urls import path

from .views import (
    SchoolListCreateAPIView, StudentListCreateAPIView, SchoolUpdateView, StudentUpdateView,
    SchoolStudentsListView
)

urlpatterns = [
    path('schools', SchoolListCreateAPIView.as_view(), name='schools'),
    path('students', StudentListCreateAPIView.as_view(), name='students'),
    path('schools/<int:pk>', SchoolUpdateView.as_view(), name='school_update'),
    path('students/<int:pk>', StudentUpdateView.as_view(), name='student_update'),
    path('schools/<int:pk>/students', SchoolStudentsListView.as_view(), name='school_students'),

]
