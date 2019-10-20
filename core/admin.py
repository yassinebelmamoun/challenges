from django.contrib import admin

from core.models import School, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
