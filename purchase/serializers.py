from rest_framework import serializers
from .models import Supplier_Detail,Individual_Detail

class Supplier_Detail_Serialize(serializers.ModelSerializer):
	class Meta:
		Model = Supplier_Detail
		fields = "__all__"

class Individual_Detail_Serialize(serializers.ModelSerializer):
	class Meta:
		Model = Individual_Detail
		fields = "__all__"
		depth = 1
