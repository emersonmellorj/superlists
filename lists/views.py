from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    
    # Primeiro teste de conteudo de retorno da view
    return HttpResponse('<html><title>To-Do lists</title></html>')