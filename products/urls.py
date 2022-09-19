
from django.urls import path, include
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(queryset=Productmaster.objects.all(), serializer_class=ProductmasterSerializer), name='Product-list'),
    path('subgroups/', SubgroupList.as_view(queryset=Subgroupmaster.objects.all(), serializer_class=SubgroupmasterSerializer), name='Subgroup-list')

]
