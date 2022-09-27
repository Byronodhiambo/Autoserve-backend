from .models import Productmaster,Subgroupmaster
from rest_framework import serializers


class ProductmasterSerializer(serializers.ModelSerializer):
      
   class Meta:
        model = Productmaster
        fields = ['id', 'productname', 'subgroupid', 'productgroupid', 'departmentid', 'picture1', 'picture2', 'price', 'trial_standardcostprice_28']
        
class SubgroupmasterSerializer(serializers.ModelSerializer):
   class Meta:
        model = Subgroupmaster
        fields = ['subgroupid', 'subgroupname', 'subgroupid', 'productgroupid']


