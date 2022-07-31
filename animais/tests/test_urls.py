from django.test import testcases
from django.urls import reverse
from animais.views import index


class AnimaisURLSTestCase(testcases):

    def test_rola_url_utiliza_view_index(self):
        """
         teste se a home da aplicao utiliza a fncao imdex da view
        :return:
        """
        root = reverse('/')
        self.assertEqual(root.func, index)