from django.contrib import admin

from my_app.models import Student, Course, User

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Course)
