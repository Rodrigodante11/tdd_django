from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):  # configurar o browser
        self.browser = webdriver.Chrome('C:\\Users\\DELL\\Desktop\\django\\tdd_django\\projeto\\chromedriver.exe')

    def tearDown(self):  # fechar a aba do chrome apos o teste
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """
        Test se um usuario encontra um animal na pesquisa
        :return:
        """

        home_page = self.browser.get(self.live_server_url + '/')
        brand_elemtent = self.browser.find_element(By.CSS_SELECTOR, 'exemplo')
        self.assertEqual('Busca Animal', brand_elemtent.text)

