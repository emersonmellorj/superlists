from django.test import TestCase
from django.urls import resolve
from .views import home_page
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
    
    # Este metodo foi utilizado no primeiro teste, nao sendo necessario posteriormente, pois esse teste esta sendo feito no metodo abaixo.
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        
        # Testando se o nome da view chamada pela URL / e a home_page
        self.assertEqual(found.func, home_page)
        
        
    def test_uses_home_template(self):
        
         response = self.client.get('/')
         # Verificar se estou recebendo o template correto na renderizacao da resposta
         self.assertTemplateUsed(response, 'home.html')  
    
    
    def test_can_save_a_POST_request(self):
        
        response=self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode()) 
        self.assertTemplateUsed(response, 'home.html') 
    
    
    # Este metodo foi substituido pelo metodo acima
    def test_home_page_returns_correct_html(self):
        
        # Primeiro test, criando a requisicao manualmente
        #request = HttpRequest()
        
        # Response = uma view criado recebendo um request como parametro
        #response = home_page(request)
        
        response = self.client.get('/')
        html = response.content.decode('UTF-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
        
        # Verificar se estou recebendo o template correto na renderizacao da resposta
        self.assertTemplateUsed(response, 'home.html')