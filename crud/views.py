from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import students
from .serializers import studentsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages

# Create your views here.
@api_view(['GET'])
def index(request):

    return HttpResponse("Welcome to website")

@api_view(['GET'])
def get_students(request):
    students_obj = students.objects.all()
    data = studentsSerializers(students_obj, many=True)
    context = {
        'students': data.data
    }

    return render(request, 'home.html', context)

@api_view(['GET','POST'])
def add_student(request):
    if request.method == 'POST' :
        student = request.data
        data = studentsSerializers(data=student)
        print(data)
        if data.is_valid():
            data.save()
        else:
            return Response('Make sure detail is correct and unique')

        return HttpResponseRedirect('/get_students/')
    return render(request, 'add_stud.html')

@api_view(['GET','POST'])
def delete_student(request, stud_id):
    student = students.objects.get(stud_id=stud_id)
    print(student.name)
    student.delete()
    return HttpResponseRedirect('/get_students/')

@api_view(['GET','POST'])
def update_student(request, stud_id):
    if request.method == 'POST':
        student = request.data
        stud_obj = students.objects.get(stud_id = stud_id)
        data = studentsSerializers(instance=stud_obj, data=student)
        if data.is_valid():
            data.save()
        else:
            return Response('Make sure detail is correct and unique')
        return HttpResponseRedirect('/get_students/')
    
    stud_obj = students.objects.get(stud_id = stud_id)
    data = studentsSerializers(stud_obj)
    return render(request, 'update_student.html', {'stud':data.data})