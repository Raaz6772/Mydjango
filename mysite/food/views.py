from django.http import HttpResponse
from .models import item
from django.template import loader
from django.shortcuts import render , redirect
from .forms import itemform
from django.contrib.auth.decorators import login_required

def index(request):
    item_list = item.objects.all()
    context={ 'item_list':item_list,
 
       
    }
    return render(request,"food/index.html",context)
def it(request):
    return HttpResponse("<h1>This is an item view<h1>")

def detail(request,item_id):
    shi=item.objects.get(pk=item_id)
    context={'shi':shi,
             
    }
    return render(request,"food/detail.html",context)

def create_form(request):
    qwer=itemform(request.POST or None)
    if qwer.is_valid():
        qwer.save()
        return redirect('food:index')
    
    return render(request,'food/item-form.html',{'qwer':qwer,})

def update_item(request,id):
    pq=item.objects.get(id=id)
    qwer=itemform(request.POST or None, instance=pq)
    if qwer.is_valid():
        qwer.save()
        return redirect('food:index')
    return render(request,'food/item-form.html',{'pq':pq,'qwer':qwer})

def delete_item(request,id):
    pq=item.objects.get(pk=id)
    if request.method=="POST":
        pq.delete()
        return redirect('food:index')
    return render(request,'food/delete-item.html',{'pq':pq})
    


        