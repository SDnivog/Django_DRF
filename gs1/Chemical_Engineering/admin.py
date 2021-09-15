from django.contrib import admin
from .models import CheStu
# Register your models here.
@admin.register(CheStu)
class CheStuAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'roll', 'mobile','email','city']