# from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer,UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':
        employee =  Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(serializer.data, safe=False)
    # return HttpResponse("Hello Empoloyee List View")
    # return JsonResponse(serializer.errors, safe=False)

def userListView(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many = True)
    return JsonResponse(serializer.data, safe=False)
