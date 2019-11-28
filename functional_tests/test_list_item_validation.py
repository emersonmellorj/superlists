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
        
        # A pagina inicial e atualizada e ha uma mensagem de erro informando que itens da lista na podem
        # estar em branco
        
        # Ela tenta novamente com um texto para um item, e isso agora funciona
        
        # De forma perversa, ela agora decide submeter um segundo item em branco na lista
        
        # Ela recebe um aviso semelhante na pagina da lista
        
        # E ela pode corrigir isso preenchendo o item com um texto
        self.fail('write me!')