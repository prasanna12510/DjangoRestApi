from rest_framework import generics
from serializers import StoreSerializer
from models import Store

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new store."""
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
	"""This class handles the http GET, PUT and DELETE requests."""

	queryset = Store.objects.all()
	serializer_class = StoreSerializer
	