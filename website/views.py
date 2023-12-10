from django.shortcuts import render

# Create your views here.

def home(request):
    isActive = True
    if request.method=='POST':
        check = request.POST.get('check')
        print(check)
        if check is not None:
            isActive = True
        else:
            isActive = False

    favourite_lang = ['Python', 'Django', 'C++']
    students = {
        'name':'Vishnu',
        'college': 'RJ',
        'Hobby':'timepass'
    }

    context = {
        'languages': favourite_lang,
        'student_data': students,
        'isActive':isActive
    }

    return render(request, 'home.html', context)

def about(request):

    return render(request, 'about.html')

def services(request):

    return render(request, 'services.html')

