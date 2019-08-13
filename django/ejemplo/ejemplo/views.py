from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    respu= "<ul>"
    respu= respu+ "<li>elemento1</li>"
    respu= respu+ "<li>elemento2</li>"
    respu= respu+ "</ul>"
    return HttpResponse(respu)

def nuevococinero(request):
    return HttpResponse("<p>este es un nuevo cocinero")

def i1(request):
    return HttpResponse("<p>1")

def i2(request):
    return HttpResponse("<p>2")

def i3(request):
    return HttpResponse("<p>3")