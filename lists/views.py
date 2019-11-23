from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List

# Create your views here.
def home_page(request):
    
    #if request.method == "POST":
        #return HttpResponse(request.POST['item_text'])
    
    #items = Item.objects.all()
    return render(request, 'home.html')
        
    #item = Item()
    #item.text = request.POST.get('item_text', '')
    #item.save()
    
    #return render(request, 'home.html', {'new_item_text': new_item_text})
    #return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', ''),})
    
    # Primeiro teste de conteudo de retorno da view
    #return HttpResponse('<html><title>To-Do lists</title></html>')
    

def view_list(request, list_id):
    
    list_ = List.objects.get(id=list_id)
    #items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'list':list_})
    
    #items = Item.objects.all()
    #return render(request, 'list.html', {'items': items})

  

def new_list(request):
    
    list_ = List.objects.create()
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text, list=list_)
    return redirect(f'/lists/{list_.id}/')
     
    

def add_item(request, list_id):
    
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')
    
    

def java_script(request):
    
    return render(request, 'javascript.html', {})