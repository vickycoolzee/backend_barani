from django.db import models

class Supplier_Detail(models.Model):
    Supplier_id = models.CharField(max_length=20,primary_key=True,on_delete=models.CASCADE)
    Supplier_name = models.CharField(max_length=50)
    Address = models.TextField()
    Contact = models.IntegerField()
    Email_id = models.EmailField()
    Nature_of_business = models.CharField(max_length=30)
    Sales_tax_register_number = models.CharField(max_length=30)
    Distributor_stockist_for = models.CharField(max_length=20)
    List_of_items_handled = models.CharField(max_length=50)
    Details_of_presnt_reputed_customers = models.CharField(max_length=50)
    Facilities_instruments_available = models.CharField(max_length=30)
    Equipments = models.CharField(max_length=50)
    Instruments = models.CharField(max_length=50)
    Any_other_information = models.TextField()
    Date = models.DateField(null=True,default=None)
    def __str__(self):
    	return self.Supplier_id


class Individual_Detail(models.Model):
    Supplier_detail = models.ForeignKey(Supplier_Detail, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Designation = models.CharField(max_length=30)
    Email_id = models.EmailField()
    Contact = models.CharField(max_length=10)
    Date = models.DateField(default = None,null=True)
    Time = models.TimeField(default = None,null=True)
    def __str__(self):
        return   self.Name