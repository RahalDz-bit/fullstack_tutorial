from django.shortcuts import render

def myapp(request) :
 
    return render(request=request, template_name='main.html',context= {'name' : 'Rahal'})