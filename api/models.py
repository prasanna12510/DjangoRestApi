
from django.db import models


class Store(models.Model):
	name = models.CharField(max_length=50)
    	buildingName = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	companyId = models.CharField(max_length=50)
	contact = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	currency = models.CharField(max_length=50)
	lat = models.DecimalField(max_digits=10,decimal_places=5)
	lng = models.DecimalField(max_digits=10,decimal_places=5)
	photo = models.CharField(max_length=50)
	streetName = models.CharField(max_length=50)
        zip = models.CharField(max_length=10)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

    	def __str__(self):
		return "{}".format(self.name)


