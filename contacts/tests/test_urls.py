from django.test import SimpleTestCase
from django.urls import reverse, resolve

from contacts.views import contact


class TestContactUrls(SimpleTestCase):

    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func, contact)
