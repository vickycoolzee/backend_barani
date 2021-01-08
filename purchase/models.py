from django.db import models

class Supplier_Detail(models.Model):
    Supplier_id = models.CharField(max_length=30,primary_key=True)
    Supplier_name = models.CharField(max_length=50)
    Address = models.TextField()
    Contact = models.CharField(max_length=10,default=None)
    Email_id = models.EmailField()
    Nature_of_business = models.CharField(max_length=30)
    GST_no = models.CharField(max_length=30)
    Distributor = models.CharField(max_length=20)
    List_of_item = models.CharField(max_length=50)
    Details  = models.TextField(default = None)
    Details_file = models.FileField(default = None)
    Facilities = models.TextField(default = None)
    Facilities_file = models.FileField(default = None)
    Information = models.TextField()
    Date = models.DateField(null=True,default=None)
    Time = models.TimeField(null = True,default = None)
    def __str__(self):
        return self.Supplier_id







