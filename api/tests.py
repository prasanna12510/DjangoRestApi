
from django.test import TestCase
from models import Store
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

# Create your tests here.

class ModelTestCase(TestCase):
	"""This class defines the test suite for store model."""

	def setUp(self):
		"""Define the test client and other test variables."""
		self.store_name = "Any store name"
		self.store_lat = "10.12"
		self.store_lng = "45.23"
		self.store = Store(name=self.store_name,lat=self.store_lat,lng=self.store_lng)


	def test_model_can_create_a_store(self):
		old_count = Store.objects.count()
		self.store.save()
		new_count = Store.objects.count()
		self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
	"""Test suite for the api views."""


	def setUp(self):
		"""Define the test client and other test variables."""
		self.client = APIClient()
		self.store_data = {'name':'Store Name','lat':'12.34','lng':'45.23'}
		self.response = self.client.post(
			reverse('create'),
			self.store_data,
			format="json")

	def test_api_can_create_a_store(self):
		"""Test the api has store creation capability."""
		self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)	

