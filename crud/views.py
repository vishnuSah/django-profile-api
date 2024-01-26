from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import students
from .serializers import studentsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

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
        
        messages.success(request, 'Details added Successfully !!')

        return HttpResponseRedirect('/get_students/')
    return render(request, 'add_stud.html')

@api_view(['GET','POST'])
def delete_student(request, stud_id):
    student = students.objects.get(stud_id=stud_id)
    print(student.name)
    student.delete()
    messages.success(request, 'Student Deleted !!')
    return HttpResponseRedirect('/get_students/')

@api_view(['GET','POST'])
def update_student(request, stud_id):
    if request.method == 'POST':
        student = request.data
        stud_obj = students.objects.get(stud_id = stud_id)
        data = studentsSerializers(instance=stud_obj, data=student)
        if data.is_valid():
            data.save()
        elif stud_id is not None:
            stud_obj = students.objects.filter(stud_id = stud_id)
            if stud_obj is not None:
                return Response('Student ID already exist')
        else:
            return Response('Make sure detail is correct and unique')
        
        messages.success(request, 'Details updated Successfully !!')
        return HttpResponseRedirect('/get_students/')
    
    stud_obj = students.objects.get(stud_id = stud_id)
    data = studentsSerializers(stud_obj)
    return render(request, 'update_student.html', {'stud':data.data})

@api_view(['GET','POST'])
def search_student(request):
    stud_name = request.POST.get('name')
    print(stud_name)
    student_obj = students.objects.filter(name__icontains=stud_name)
    if student_obj != None:
        data = studentsSerializers(student_obj, many=True)
        print(data.data)
        context = {
            'students': data.data
        }
    
        return render(request, 'search.html', context)
    else:
        return Response("No Data Found")
        
@api_view(['GET','POST'])
def register(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        #print(request.data)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully !!")


    context = {
        'form': form
    }

    return render(request, 'register.html', context)

@api_view(['GET','POST'])
def perform_login(request):

    form = CreateUserForm()

    context = {
        'form':form
    }
    
    return render(request, 'login.html', context)