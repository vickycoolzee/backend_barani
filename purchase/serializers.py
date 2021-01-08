from rest_framework import serializers
from .models import Supplier_Detail

class Supplier_Detail_Serialize(serializers.ModelSerializer):
	class Meta:
		model = Supplier_Detail
		fields = "__all__"
