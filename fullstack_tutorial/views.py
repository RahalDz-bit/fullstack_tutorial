from django.shortcuts import render
from . import database
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status

def myapp(request) :
 
    return render(request=request, template_name='main.html',context= {'name' : 'Rahal'})

@api_view(["GET", "POST"])
def getData(request) :
    if request.method == "GET" :
        data = database.podex
        return Response(data)
    elif request.method == "POST" :
        data = request.data
        number = data.get('number')
        try :
            
            parsedNumber = int(number)
            
            reponseData = {'pokemon': database.podex[str(parsedNumber)], 'status': 'success'}
            
        except :
            print("Error")
            reponseData = {'message': 'Invalid number', 'status': 'error'}
        return Response(reponseData, status=status.HTTP_201_CREATED)



