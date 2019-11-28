#######################################
## Functional Tests fo application
#######################################

from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

                
class NewVisitorTest(FunctionalTest):
#class NewVisitorTest(unittest.TestCase):
            
    def test_can_start_a_list_for_one_user(self):
        # Edith ouviu falar de uma nova aplicacao online interessante para lista de tarefas. Ela decide verificar sua HP.
        self.browser.get(self.live_server_url)
        #self.browser.get('http://localhost:8000')

        # Ela percebe que o titulo da pagina e cabecalho mencionam listas de tarefas (to-do).
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        time.sleep(3)
        
        # Ela e convidada a inserir um item de tarefa imediatamente.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        time.sleep(3)
        
        # Ela digita "Buy peacock feathers" em uma caixa de texto (o hobby dela e fazer iscas de peixe com fly).
        inputbox.send_keys('1 - Buy peacock feathers')
        time.sleep(3)

        # Quando ela tecla enter, a pagina e atualizada, e agora a pagina lista "1: Buy peacock feathers" com um item em uma lista de tarefas
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1 - Buy peacock feathers')
        #self.assertTrue(any(row.text == '1 - Buy peacock feathers' for row in rows), f"New to-do item not appear in table. Contents were: \n{table.text}")
        
        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item. Ela insere "Use peacock feathers to make a fly". Edith e bem metodica.
        inputbox = self.browser.find_element_by_id('id_new_item')
        
        inputbox.send_keys('2 - Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        # A pagina e atualizada novamente e agora mostra os dois itens em sua lista.
        self.wait_for_row_in_list_table('1 - Buy peacock feathers')
        self.wait_for_row_in_list_table('2 - Use peacock feathers to make a fly')
        
        # Edith se pergunta se o site lembrara da sua lista. Entao ela nota que o site gerou uma URL unica pra ela -- ha um pequeno texto explicativo para isso.
        #self.fail('Finish the test!')

        # Ela acessa essa URL - sua lista de tarefas continua la.

        # Satisfeita, ela volta a dormir.

    
    def test_multiple_users_can_start_lists_at_different_urls(self):
        
        # Edith inicia uma nova lista de tarefas
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys('1 - Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1 - Buy peacock feathers')
        
        # Ela percebe que sua lista tem um URL unico
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        
        # Agora um novo usuario, Francis, chega ao site.
        
        ## Usamos uma nova sessao de navegador para garantir que nenhuma informacao de Edith esta vindo de cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        # Francis acessa a pagina inicial. Nao ha nenhum sinal da lista de Edith
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name("body").text
        print(page_text)
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        
        # Francis inicia uma nova lista inserindo um item novo. Ele é menos interessante que Edith
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys('1 - Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1 - Buy milk')
        
        # Francis obtem o seu proprio URL exclusivo
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        
        # Novamente nao ha nenhum sinal da lista de Edith
        page_text = self.browser.find_element_by_tag_name("body").text
        print(page_text)
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        
        # Satisfeitos, ambos voltam a dormir
