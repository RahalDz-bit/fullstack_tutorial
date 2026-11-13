from django.shortcuts import render
from . import database
from rest_framework.response import Response 
from rest_framework.decorators import api_view

def myapp(request) :
 
    return render(request=request, template_name='main.html',context= {'name' : 'Rahal'})

@api_view(['GET', 'POST'])
def getData(request) :
    data  = database.podex
    return Response(data)

def podex(request) :
 
    return render(request=request, template_name='nigga.html')


