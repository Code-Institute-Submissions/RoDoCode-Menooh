from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def contact_us(request):
    if request.method == "GET":
        return HttpResponse("This will be the contact user-support form")
    elif request.method == "POST":
       return HttpResponse("This was a POST request")
    else:
        return Httpresponse("This was neither GET nor POST")
