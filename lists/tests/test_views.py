from django.test import TestCase
from django.urls import resolve
from lists.views import home_page, java_script
from django.http import HttpRequest
from lists.models import Item, List
from django.utils.html import escape
from lists.forms import ItemForm
from unittest import skip

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
    

    def test_home_page_uses_item_form(self):

        response = self.client.get('/')
        self.assertIsInstance(response.context['form'], ItemForm)

        
    # Este metodo foi substituido pelo metodo acima
    def test_home_page_returns_correct_html(self):
        
        # Primeiro test, criando a requisicao manualmente
        #request = HttpRequest()
        
        # Response = uma view criado recebendo um request como parametro
        #response = home_page(request)
        
        response = self.client.get('/')
        html = response.content.decode('UTF-8')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
        
        # Verificar se estou recebendo o template correto na renderizacao da resposta
        self.assertTemplateUsed(response, 'home.html')
    
    

    # Teste desativado    
    @skip
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
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')
        #self.assertEqual(response.status_code, 302)
        #self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
        
    
    def test_validation_errors_are_sent_back_to_home_page_template(self):
        
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        expected_error = escape("You can't have an empty list item")
        #print(response.content.decode())
        self.assertContains(response, expected_error)
    
    
    def test_invalid_list_items_arent_saved(self):
        
        self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)



class ListViewTest(TestCase):
    
    def test_display_only_items_for_that_list(self):
        
        correct_list = List.objects.create()
        Item.objects.create(text='item 1', list = correct_list)
        Item.objects.create(text='item 2', list = correct_list)
        
        other_list = List.objects.create()
        Item.objects.create(text='other text item 1', list = other_list)
        Item.objects.create(text='other text item 2', list = other_list)
        
        response = self.client.get(f'/lists/{correct_list.id}/')
        #print("Correct List Id: {}".format(correct_list.id))
        
        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')
        
        self.assertNotContains(response, 'other text item 1')
        self.assertNotContains(response, 'other text item 2')
        
        
    def test_passes_correct_list_to_template(self):
        
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f'/lists/{correct_list.id}/')
        
        self.assertEqual(response.context['list'], correct_list)
        
    
    def test_can_save_a_POST_request_to_an_existing_list(self):
        
        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        self.client.post(f'/lists/{correct_list.id}/', data={'item_text': 'A new item for an existing list'})
        
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)
    
    
    def test_POST_redirects_to_list_view(self):
        
        other_list = List.objects.create()
        correct_list = List.objects.create()
        
        response = self.client.post(f'/lists/{correct_list.id}/', data={'item_text': 'A new item for an existing list'}) 
        
        self.assertRedirects(response, f'/lists/{correct_list.id}/')
    
    
    def test_validation_errors_end_up_on_lists_page(self):
        
        list_ = List.objects.create()
        response = self.client.post(f'/lists/{list_.id}/', data={'item_text': ''})
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)
    
    
    def test_validate_if_empty_text_can_save(self):
        
        list_ = List.objects.create()
        self.client.post(f'/lists/{list_.id}/', data={'item_text': '1 - A new item for an existing list'})
        self.client.post(f'/lists/{list_.id}/', data={'item_text': '2 - A new item for an existing list'})
        self.client.post(f'/lists/{list_.id}/', data={'item_text': ''})
        
        self.assertEqual(Item.objects.count(), 2)
                



class EstudoJavaScript(TestCase):
    
    def test_url_return_correct_template(self):
        
        found = resolve('/java_script/')
        
        # Testando se o nome da view chamada pela URL / e a home_page
        self.assertEqual(found.func, java_script)
        
        response = self.client.get('/java_script/')
        html = response.content.decode('UTF-8')
        
        self.assertIn('Pagina de Estudo de JavaScript', html)
        self.assertTemplateUsed(response, 'javascript.html')