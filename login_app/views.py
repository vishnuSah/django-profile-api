from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.decorators import permission_classes, authentication_classes, api_view
from rest_framework.authtoken.models import Token
import requests
# Create your views here.
def render_login(request):

    return render(request, 'login.html')

@api_view(['POST'])
def perform_login(request):
    if request.method != 'POST':
        return HttpResponse("Method Not allowed")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            token, created= Token.objects.get_or_create(user=user_obj)
            print(token)
            admin_dashboard_url = request.build_absolute_uri(reverse('admin_dashboard'))
            headers = {'Authorization': f'Token {token}'}
            response = requests.get(admin_dashboard_url, headers=headers)

            # Check if the API call was successful (status code 200)
            if response.status_code == 200:
                django_response = HttpResponse(content=response.content, status=response.status_code)
                django_response['Content-Type'] = response.headers['Content-Type']
                return django_response
            else:
                # Handle error accordingly
                messages.error(request, "Failed to authenticate")
                return HttpResponse("Failed to authenticate", status=response.status_code)
        else:
            messages.error(request,"Username or password invalid")
            return HttpResponseRedirect("/")

@api_view(['GET'])
@authentication_classes((TokenAuthentication,))  
@permission_classes((IsAuthenticated,))      
def admin_dashboard(request):
    print(f'User: {request.user}')
    context = {
        'user': request.user 
    }
    return render(request, 'admin_dashboard.html', context)

def perform_register(request):
    if request.method != 'POST':
        return render(request, 'register.html')
    else:
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return HttpResponseRedirect(reverse('render_login'))
        except Exception as e:
            print(e)
            
def perform_logout(request):
    logout(request)
    return HttpResponse("Logged Out ! Visit again ")


