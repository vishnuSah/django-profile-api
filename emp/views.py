from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Emp
import json
# Create your views here.

def emp_home(request):

    emps = Emp.objects.all()
    context = {
        'emps':emps
    }

    return render(request, 'emp/home.html', context)

def add_emp(request):

    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        emp_id = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')
        if emp_working is None:
            emp_working = False
        else:
            emp_working = True
        emp_department = request.POST.get('emp_department')

        emp = Emp(name=emp_name,emp_id=emp_id,phone=emp_phone,address=emp_address,working=emp_working,department=emp_department)
        emp.save()
        print("saved")
        return redirect('/emp/home/')

    return render(request, 'emp/add_emp.html', {})

def delete_emp(request, emp_id):
    print(emp_id)
    emp = Emp.objects.get(pk=emp_id)
    emp.delete()
    print('Deleted')

    return redirect('/emp/home/')

def update_emp(request, emp_id):
    if request.method == 'POST':
        emp_name = request.POST.get('emp_name')
        emp_id_temp = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')
        if emp_working is None:
            emp_working = False
        else:
            emp_working = True
        emp_department = request.POST.get('emp_department')

        e = Emp.objects.get(pk=emp_id)
        e.name = emp_name
        e.emp_id = emp_id_temp
        e.phone = emp_phone
        e.address = emp_address
        e.working = emp_working
        e.department = emp_department

        e.save()
        print("saved")
        return redirect('/emp/home/')

    print(emp_id)
    emp = Emp.objects.get(pk=emp_id)
    print(emp.name)
    context = {
        'emp':emp
    }

    return render(request,'emp/update_emp.html', context)


   
