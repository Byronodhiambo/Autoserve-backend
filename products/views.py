from rest_framework import viewsets
from .serializers import ProductmasterSerializer, SubgroupmasterSerializer
from .models import Productmaster,Subgroupmaster
from rest_framework import filters
from rest_framework import generics

# Create your views here.

class ProductList(generics.ListAPIView):
    queryset = Productmaster.objects.all()
    serializer_class = ProductmasterSerializer
    lookup_field = 'productname'
    filterset_fields = ('subgroupid','productname')
    search_fields = ('subgroupid__subgroupname','productname',)

class SubgroupList(generics.ListAPIView):
    queryset = Subgroupmaster.objects.all()
    serializer_class = SubgroupmasterSerializer
    lookup_field = 'subgroupname'
    