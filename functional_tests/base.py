#######################################
## Functional Tests fo application
#######################################

import unittest
from selenium import webdriver
import time
#from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
import os
from selenium.webdriver.firefox.options import Options


MAX_WAIT = 10


class FunctionalTest(StaticLiveServerTestCase):
    
    def setUp(self):
        #options = Options()
        #options.add_argument('-headless')
        #self.browser = webdriver.Firefox(options=options)
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get('STAGING_SERVER')
        if staging_server:
            self.live_server_url = 'http://' + staging_server

    def tearDown(self):
        self.browser.quit()
    
    # Esta funcao ira verificar se a string digitada se encontra carregada dentro da row da pagina
    def wait_for_row_in_list_table(self, row_text):
        
        start_time = time.time()
        while True:
        
            try:
        
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            
            except (AssertionError, WebDriverException) as e:
                
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)


    def wait_for(self, fn):
        
        start_time = time.time()
        while True:
        
            try:
                
                return fn()
            
            except (AssertionError, WebDriverException) as e:
                
                if time.time() - start_time > MAX_WAIT:
                    raise e
                print(f'{time.time()} - {start_time}')
                time.sleep(0.5)

    
    def get_item_input_box(self):

        return self.browser.find_element_by_id('id_text')


 # Este if nao e mais necessario, pois estamor utilizando o servidor de testes do Django               
if __name__ == '__main__':
    unittest.main(warnings='ignore')
