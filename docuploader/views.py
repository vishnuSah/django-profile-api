from rest_framework import response
from django.http import HttpResponse

def hello(request):

    return HttpResponse("Welcome !!!")