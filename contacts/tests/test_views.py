from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from contacts.models import Contact
import datetime as dt

CONTACT_URL = reverse('contact')


# class TestContacsViews(TestCase):

#     def test_create_contact_not_user(self):
#         """Test the creation of a listings contact."""
#         payload = {
#             'id': 2,
#             'listing_id': 5,
#             'listing': "12 United Road",
#             'name': 'Andrea Pérez',
#             'email': 'test@londonappdev.com',
#             'phone': '333-333-3333',
#             'message': '',
#             'user_id': '3',
#             'realtor_email': 'test@gmail.com',
#             'contact_date': '2019-11-07 18:41:35.508501+01',
#         }
#         response = self.client.post(CONTACT_URL, payload)

#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse(
#             '/listing/'+'<int:listing_id>'))
        # contact = Contact.objects.get(id=response.data['id'])
        # for key in payload.keys():
        #     self.assertEqual(payload[key], getattr(contact, key))
