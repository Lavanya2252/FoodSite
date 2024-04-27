from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.template import loader
# Create your views here.

def index(request):
    all_items = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'all_items': all_items
    }
    return HttpResponse(template.render(context, request))

def details(request, item_id):
    curr_item = Item.objects.get(pk=item_id)
    context = {'curr_item': curr_item}
    return render(request, 'food/details.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/create_item.html', {'form': form})

def delete_item(request, id):
    del_item = Item.objects.get(pk=id)
    if request.method == 'POST':
        del_item.delete()
        return redirect('food:index')
    return render(request, 'food/confirm_delete.html', {'curr_item': del_item})

def update_item(request, id):
    curr_item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=curr_item) # passing the current item values to pre-populate  
    if form.is_valid():
        form.save()
        return redirect('food:index')  
    return render(request, 'food/create_item.html', {'form': form})