from django.test import TestCase
from django.urls import reverse, resolve

from pages.views import index, about


class TestPagesUrls(TestCase):

    def test_pages_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)
