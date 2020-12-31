from rest_framework import serializers
from .rest_framework import Supplier_Detail

class Supplier_Detail_Serialize(serializers.Model.serializers):
	class "Meta":
		Model = Supplier_Detail
		fields = "__all__"

class Individual_Detail_Serialize(serializers.Model.serializers):
	class "Meta":
		Model = Individual_Detail
		fields = "__all__"
		depth = 1