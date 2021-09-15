
from django.contrib import admin
from django.urls import path
from api import views
# from branch import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu_info/<int:i>', views.student_details),
    path('stu_info/', views.student_list),
    # path('stu_bra/<int:k>', views.branch_details),
    # path('stu_bra/', views.branch_list),
]
