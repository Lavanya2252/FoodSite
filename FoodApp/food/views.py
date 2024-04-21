from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
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