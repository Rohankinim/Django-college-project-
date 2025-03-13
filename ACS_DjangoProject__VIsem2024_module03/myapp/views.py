# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data here
            return HttpResponse('Thank you for your message.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
