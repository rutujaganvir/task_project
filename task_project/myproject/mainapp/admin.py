from django.contrib import admin
from .models import School, Student

# Register your models here.

# class SchoolAdmin(admin.ModelAdmin):
#     list_display = ["name", "created_at", "updated_at"]


admin.site.register(School)
admin.site.register(Student)
