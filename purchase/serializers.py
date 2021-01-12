from rest_framework import serializers
from .models import Supplier_Detail,Supplier_Evaluation,Supplier_rating

class Supplier_Detail_Serialize(serializers.ModelSerializer):
	class Meta:
		model = Supplier_Detail
		fields = "__all__"

class Supplier_Evaluation_Serialize(serializers.ModelSerializer):
	class Meta:
		model = Supplier_Evaluation
		fields = "__all__"

class Supplier_rating_Serialize(serializers.ModelSerializer):
	class Meta:
		model = Supplier_rating
		fields = '__all__'
