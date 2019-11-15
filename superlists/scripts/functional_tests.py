#######################################
## Functional Tests fo application
#######################################

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
        
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith ouviu falar de uma nova aplicacao online interessante para lista de tarefas. Ela decide verificar sua HP.
        self.browser.get('http://localhost:8000')

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
        time.sleep(3)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        #self.assertTrue(any(row.text == '1 - Buy peacock feathers' for row in rows), f"New to-do item not appear in table. Contents were: \n{table.text}")
        self.assertIn('1 - Buy peacock feathers', [row.text for row in rows])
        
        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro item. Ela insere "Use peacock feathers to make a fly". Edith e bem metodica.
        inputbox = self.browser.find_element_by_id('id_new_item')
        time.sleep(3)
        inputbox.send_keys('2 - Use peacock feathers to make a fly')
        time.sleep(3)
        
        inputbox.send_keys(Keys.ENTER)
        time.sleep(3)
        
        # A pagina e atualizada novamente e agora mostra os dois itens em sua lista.
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        
        self.assertIn('1 - Buy peacock feathers', [row.text for row in rows])
        self.assertIn('2 - Use peacock feathers to make a fly', [row.text for row in rows])

        # Edith se pergunta se o site lembrara da sua lista. Entao ela nota que o site gerou uma URL unica pra ela -- ha um pequeno texto explicativo para isso.
        self.fail('Finish the test!')

        # Ela acessa essa URL - sua lista de tarefas continua la.

        # Satisfeita, ela volta a dormir.

                
if __name__ == '__main__':
    unittest.main(warnings='ignore')