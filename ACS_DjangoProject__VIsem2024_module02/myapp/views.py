from django.shortcuts import render, redirect
from .forms import ItemForm
from django.http import HttpResponse

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_success')
    else:
        form = ItemForm()
    return render(request, 'item_form.html', {'form': form})

def item_success(request):
    return HttpResponse("Item created successfully!")
