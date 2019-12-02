from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, List
from django.core.exceptions import ValidationError

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
    error = None
    #items = Item.objects.filter(list=list_)
    
    if request.method == "POST":
        
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            #address = '/lists/{}/'.format(list_.id)
            return redirect(list_)
    
        except ValidationError:
            error = "You can't have an empty list item"
    
    return render(request, 'list.html', {'list':list_, 'error': error})
    
    #items = Item.objects.all()
    #return render(request, 'list.html', {'items': items})

  

def new_list(request):
    
    list_ = List.objects.create()
    new_item_text = request.POST['item_text']
    item = Item.objects.create(text=new_item_text, list=list_)
    
    # Validando se o valor do item recebido e vazio
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error': error})
        
    #return redirect(f'/lists/{list_.id}/')
    #address = '/lists/{}/'.format(list_.id)

    # Function reverse url by Django
    return redirect(list_)
     
    

#def add_item(request, list_id):
    
#    list_ = List.objects.get(id=list_id)
#    Item.objects.create(text=request.POST['item_text'], list=list_)
    # return redirect(f'/lists/{list_.id}/')
#    address = '/lists/{}/'.format(list_.id)
#    return redirect(address)
    
    

def java_script(request):
    
    return render(request, 'javascript.html', {})