from django.contrib import admin
from .models import Degree, Student, Course, Tuition
from dataclasses import fields 
# Register your models here.

class DegreeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'duration')
    search_fields = ['name', 'code']
    list_filter =[ 'duration']

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'degree', 'is_active')
    list_filter =[ 'degree', 'is_active']

class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'teacher')
    search_fields = ['name', 'code']

class TutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course')
    

admin.site.register(Degree, DegreeAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Tuition, TutionAdmin)
