#from rest_framework.serializers import Serializer
#from .models import Student
from django.shortcuts import render
from .models import Branch
from .serializers import BranchSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Create your views here.

# Model Object - Single Student Data
def branch_details(request,i):
    stu = Branch.objects.get(id = i)
    serializer = BranchSerializer(stu)
    #json_data = JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

    # Model Object - Single Student Data
# def branch_list(request):
#     stu = Branch.objects.all()
#     serializer = BranchSerializer(stu, many=True)
#     #json_data = JSONRenderer().render(serializer.data)
#     #return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data, safe=False)