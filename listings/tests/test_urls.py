from django.test import TestCase
from django.urls import reverse, resolve

from listings.views import listing, search, index


class TestListingsUrls(TestCase):

    def test_index_url_resolves(self):
        url = reverse('listings')
        self.assertEqual(resolve(url).func, index)

    def test_search_url_resolves(self):
        url = reverse('search')
        self.assertEqual(resolve(url).func, search)

    def test_single_listing_url_resolves(self):
        url = reverse('listing', args=[1, ])
        self.assertEqual(resolve(url).func, listing)
