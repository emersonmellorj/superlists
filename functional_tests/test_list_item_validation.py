#######################################
## Functional Tests fo application
#######################################

from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
   
    def test_cannot_add_empty_list_items(self):
        
        # Edith acessa a pagina inicial e acidentalmente tentar submeter um item vazio na lista.
        # Ela tecla enter na caixa de entrada vazia
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        
        # A pagina inicial e atualizada e ha uma mensagem de erro informando que itens da lista na podem
        # estar em branco
        self.wait_for(lambda: self.assertEqual(self.browser.find_element_by_css_selector('.has-error').text,
                        "You can't have an empty list item"))
        
        # Ela tenta novamente com um texto para um item, e isso agora funciona
        self.browser.find_element_by_id('id_new_item').send_keys('1 - Buy milk')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1 - Buy milk')
        
        # De forma perversa, ela agora decide submeter um segundo item em branco na lista
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        
        # Ela recebe um aviso semelhante na pagina da lista
        self.wait_for(lambda: self.assertEqual(self.browser.find_element_by_css_selector('.has-error').text,
                        "You can't have an empty list item"))
        
        # E ela pode corrigir isso preenchendo o item com um texto
        self.browser.find_element_by_id('id_new_item').send_keys('2 - Make tea')
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1 - Buy milk')
        self.wait_for_row_in_list_table('2 - Make tea')
        
        self.fail('write me!')