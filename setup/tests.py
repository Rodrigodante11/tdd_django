from django.test import LiveServerTestCase
from selenium import webdriver


class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.broser = webdriver.Chrome('C:\\Users\\DELL\\Desktop\\django\\tdd_django\\projeto\\chromedriver.exe')
