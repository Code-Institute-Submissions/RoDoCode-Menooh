from django.shortcuts import render
from .models import Contact


def contact_us(request):
    """
    Renders the About page
    """
    contact = Contact.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "contact/contact.html",
        {"contact": contact},
    )
