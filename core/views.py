from django.shortcuts import render
from django.http import HttpResponse
def core(request):
    return HttpResponse("Hello, world. You're at the polls core.")
# Create your views here.
