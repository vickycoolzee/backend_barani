from django.db import models

# Create your models here.
class Customer_Detail(models.Model):
    Customer_id = models.CharField(primary_key=True,max_length=60)
    Customer_name = models.CharField(max_length=100)
    Nick_name = models.CharField(max_length=30)
    Address = models.TextField()
    GST_no = models.CharField(max_length=30)
    CIN_no = models.CharField(max_length=30)
    Date = models.DateField(default = None,null=True)
    Time = models.TimeField(default = None,null=True)
    def __str__(self):
        return self.Customer_id


class Order_Detail(models.Model):
    Customer_id = models.ForeignKey(Customer_Detail,on_delete=models.CASCADE)
    Ventor_code = models.CharField(max_length=15,null=True)
    Part_code = models.CharField(max_length=15)
    Part_name = models.CharField(max_length=15)
    Casting_type = models.CharField(max_length=15)
    Pattern_scope= models.CharField(max_length=20)
    Transport = models.CharField(max_length=20,null=True)
    Painting_method = models.CharField(max_length=20,null=True)
    Packing_type = models.CharField(max_length=24,null=True)
    Machinary_type = models.CharField(max_length=24,null=True)
    Payment_terms = models.CharField(max_length=24,null=True)
    Export_required = models.CharField(max_length=5)
    Payments_terms_days = models.CharField(max_length=10,default = None,null=True)
    Quantity = models.CharField(max_length=10)
    Date = models.DateField(default = None,null=True)
    Time = models.TimeField(default = None,null=True)


class Individual_Detail(models.Model):
    Customer_id = models.ForeignKey(Customer_Detail, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Designation = models.CharField(max_length=30)
    Email_id = models.EmailField()
    Contact = models.CharField(max_length=10)
    Date = models.DateField(default = None,null=True)
    Time = models.TimeField(default = None,null=True)