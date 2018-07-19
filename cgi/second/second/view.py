from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    with open('templates/index.html','rb') as f:
        html = f.read()
#    return render(request, 'index.html')
    return HttpResponse(html)