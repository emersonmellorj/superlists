from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import Item

# Create your views here.
def home_page(request):
    
    #if request.method == "POST":
        #return HttpResponse(request.POST['item_text'])

    if request.method == 'POST':
        
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
        
    #item = Item()
    #item.text = request.POST.get('item_text', '')
    #item.save()
    
    #return render(request, 'home.html', {'new_item_text': new_item_text})
    #return render(request, 'home.html', {'new_item_text': request.POST.get('item_text', ''),})
    
    # Primeiro teste de conteudo de retorno da view
    #return HttpResponse('<html><title>To-Do lists</title></html>')