from django.contrib import admin
from .models import Students
#from .models import Faculty
# Register your models here.
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'roll', 'mobile','email','branch','city']
#  list_display = ['id', 'name','mobile','email','subject']
 
#  @admin.register(Faculty)
# class FacultyAdmin(admin.ModelAdmin):
#  list_display = ['id', 'name','mobile','email','subject']
