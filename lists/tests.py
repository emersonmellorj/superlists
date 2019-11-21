from django.test import TestCase
from django.urls import resolve
from .views import home_page, java_script
from django.http import HttpRequest
from .models import Item, List

# Create your tests here.
class ListViewTest(TestCase):
    
    # Este metodo foi utilizado no primeiro teste, nao sendo necessario posteriormente, pois esse teste esta sendo feito no metodo abaixo.
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        
        # Testando se o nome da view chamada pela URL / e a home_page
        self.assertEqual(found.func, home_page)
        
        
    def test_uses_home_template(self):
        
         response = self.client.get('/')
         # Verificar se estou recebendo o template correto na renderizacao da resposta
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
    
    
    #def test_only_saves_items_where_necessary(self):
        
    #    self.client.get('/')
    #    self.assertEqual(Item.objects.count(), 0)
    
    
    
    def test_display_all_list_items(self):
        
        Item.objects.create(text='item 1')
        Item.objects.create(text='item 2')
        
        response = self.client.get('/lists/the-only-list-in-the-world/')
        
        self.assertIn('item 1', response.content.decode())
        self.assertIn('item 2', response.content.decode())
        
    
    
class NewListTest(TestCase):
    
    def test_can_save_a_POST_request(self):
        
        response=self.client.post('/lists/new', data={'item_text': 'A new list item'})
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        
        #self.assertIn('A new list item', response.content.decode()) 
        #self.assertTemplateUsed(response, 'home.html')
    
    
    def test_redirect_after_POST(self):
        
        response=self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
        
    
        
# Second class        
class ListAndItemModelTest(TestCase):
    
    def test_saving_and_retieving_items(self):
        
        list_ = List()
        list_.save()
        
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()
        
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()
        
        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)
        


class ListViewTest(TestCase):
    
    def test_displays_all_items(self):
        
        list_ = List.objects.create()
        Item.objects.create(text='item 1', list = list_)
        Item.objects.create(text='item 2', list = list_)
        
        response = self.client.get('/lists/the-only-list-in-the-world/')
        
        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')
        
        
    def test_uses_list_template(self):
        
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    

class EstudoJavaScript(TestCase):
    
    def test_url_return_correct_template(self):
        
        found = resolve('/java_script/')
        
        # Testando se o nome da view chamada pela URL / e a home_page
        self.assertEqual(found.func, java_script)
        
        response = self.client.get('/java_script/')
        html = response.content.decode('UTF-8')
        
        self.assertIn('Pagina de Estudo de JavaScript', html)
        self.assertTemplateUsed(response, 'javascript.html')