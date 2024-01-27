from django.shortcuts import render
from .models import Contact
from .forms import CollaborateForm


def contact_us(request):
    """
    Renders the About page
    """
    contact = Contact.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "contact/contact.html",
        {"contact": contact,
         "collaborate_form": collaborate_form},
    )
