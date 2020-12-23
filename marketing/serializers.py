from rest_framework import serializers
from .models import  Customer_Detail,Order_Detail,Individual_Detail

class Customer_Detail_Serialize(serializers.ModelSerializer):
    class Meta:
        model = Customer_Detail
        fields = "__all__"
class Order_Detail_Serialize(serializers.ModelSerializer):
    class Meta:
        model = Order_Detail
        fields = "__all__"
        depth = 1

class Individual_Detail_Serialize(serializers.ModelSerializer):
    class Meta:
        model = Individual_Detail
        fields = "__all__"
        depth = 1