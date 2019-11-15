from django.test import TestCase
from django.urls import resolve
from .views import home_page
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        
        # Testando se o nome da view chamada pela URL / e a home_page
        self.assertEqual(found.func, home_page)
        
    
    def test_home_page_returns_correct_html(self):
        
        request = HttpRequest()
        
        # Response = uma view criado recebendo um request como parametro
        response = home_page(request)
        html = response.content.decode('UTF-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))