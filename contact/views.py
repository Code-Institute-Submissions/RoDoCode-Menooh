from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import CollaborateForm


def contact_us(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration \
                                 request received! I endeavour to respond \
                                 within 2 working days.")
    contact = Contact.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
    return render(
        request,
        "contact/contact.html",
        {"contact": contact,
         "collaborate_form": collaborate_form},
    )
