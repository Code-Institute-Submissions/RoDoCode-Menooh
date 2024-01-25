from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def contact_us(request):

    contact = Contact.objects.all().order_by('-updated_on').first()

    if request.method == "GET":
        return render(
            request,
            "contact/contact.html",
            {"contact": contact},
        )
    elif request.method == "POST":
        return HttpResponse("This was a POST request")
    else:
        return Httpresponse("This was neither GET nor POST")
