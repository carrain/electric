# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
#    context          = {}
#    context['hello'] = 'Hello World!'
#    return render(request, 'hello.html', context)
    

    data = "this is data from mysql"
    return render(request, 'hello.html', {'data': data})