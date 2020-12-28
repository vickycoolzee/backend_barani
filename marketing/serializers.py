from rest_framework import serializers
from .models import  Customer_Detail,Order_Detail,Individual_Detail,Product_Detail,Feasibility_Detail

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

class Product_Detail_Serialize(serializers.ModelSerializer):
    class Meta:
        model = Product_Detail
        fields = "__all__"
        depth = 2

class Feasibility_Detail_Serialize(serializers.ModelSerializer):
    class Meta:
        model = Feasibility_Detail
        fields = "__all__"
        depth = 2