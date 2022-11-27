from django.contrib import admin
from course_app.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
