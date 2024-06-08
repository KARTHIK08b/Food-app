from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader

# Create your views here.
#content user is gonna view 
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list' : item_list,
    }
    # return HttpResponse(item_list)
    # return HttpResponse(template.render(context,request))
    return render(request,'food/index.html', context )

def items(request):
    return HttpResponse('These are your items') 

def detail(request, item_id):
    item = Item.objects.get(pk = item_id)
    context = {
        'item': item, 
    }
    return render(request, 'food/detail.html', context)
    # return HttpResponse("This is item no/id: %s" %item_id)
