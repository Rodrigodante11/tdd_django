from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):  # configurar o browser
        self.browser = webdriver.Chrome('C:\\Users\\DELL\\Desktop\\django\\tdd_django\\projeto\\chromedriver.exe')

    def tearDown(self):  # fechar a aba do chrome apos o teste
        self.browser.quit()

    def test_abri_janela_do_chrome(self):
        # self.browser.get('https://www.alura.com.br/')
        self.browser.get(self.live_server_url)

    def test_falhador(self):
        """ teste exemplo de erro
        """

        self.fail('TESTE FALHOU')

    def test_buscando_um_novo_animal(self):
        """
        Test se um usuario encontra um animal na pesquisa
        :return:
        """