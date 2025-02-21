from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

# import the Contact model, the name should be the same as the class name in models.py!!!

# Create your views here.


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("name:", form.cleaned_data["name"])
            print("age:", form.cleaned_data["age"])
            print("email:", form.cleaned_data["email"])
            print("message/opinion:", form.cleaned_data["message"])
            Contact.objects.create(
                name=form.cleaned_data["name"],
                age=form.cleaned_data["age"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"],
            )
            return render(request, "success.html")

    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
