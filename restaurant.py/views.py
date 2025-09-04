from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ConatctFrom(request.POST)
        if form.is_valid():
            from.save()
            return redirect('contact')
    else:
        form = ConatactForm()
    return render(request, "contact.html",{"form":form})   