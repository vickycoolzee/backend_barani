from django.contrib import admin
from .models import Order_Detail,Customer_Detail,Individual_Detail
# Register your models here.
admin.site.register(Customer_Detail)
admin.site.register(Order_Detail)
admin.site.register(Individual_Detail)