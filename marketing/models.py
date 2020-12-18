from django.db import models

# Create your models here.
class Customer_Detail(models.Model):
    Customer_id = models.CharField(primary_key=True,max_length=60)
    Email_id = models.EmailField()
    Customer_name = models.CharField(max_length=50)
    Nick_name = models.CharField(max_length=30)
    Address = models.TextField()
    GST_no = models.CharField(max_length=30)
    CIN_no = models.CharField(max_length=30)
    Contact_1 = models.CharField(max_length= 10)
    Contact_2 = models.CharField(max_length=10)
    Contact_3 = models.CharField(max_length=10)
    Contact_4 = models.CharField(max_length=10)



