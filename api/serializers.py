
from rest_framework import serializers
from models import Store


class StoreSerializer(serializers.ModelSerializer):
	"""Serializer to map the Model instance into JSON format."""


	class Meta:
		"""Meta class to map serializer's fields with model fields."""
		model = Store
		fields = ('id','name','buildingName','city','companyId','contact','country','currency','lat','lng','photo','streetName','zip')
		read_only_fields = ('date_created', 'date_modified')