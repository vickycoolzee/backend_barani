from rest_framework import serializers
from .models import  Customer_Detail

class Customer_Detail_Serialize(serializers.ModelSerializer):
    class Meta:
        model = Customer_Detail
        fields = "__all__"
