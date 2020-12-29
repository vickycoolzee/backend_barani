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



class Individual_Detail(models.Model):
    Customer_detail = models.ForeignKey(Customer_Detail, on_delete=models.CASCADE)
    Name = models.CharField(max_length=30)
    Designation = models.CharField(max_length=30)
    Email_id = models.EmailField()
    Contact = models.CharField(max_length=10)
    Date = models.DateField(default = None,null=True)
    Time = models.TimeField(default = None,null=True)
    def __str__(self):
        return  self.Customer_id + self.Name


class Order_Detail(models.Model):
    RFQ_id= models.CharField(max_length=20,primary_key = True)
    Customer_detail = models.ForeignKey(Customer_Detail,on_delete=models.CASCADE)
    Date = models.DateField(default=None, null=True)
    Time = models.TimeField(default=None, null=True)


class Product_Detail(models.Model):
    Product_id = models.CharField(max_length=30,primary_key=True,default = 'None')
    RFQ_detail = models.ForeignKey(Order_Detail,on_delete=models.CASCADE,default=None)
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
    Is_feasiable = models.BooleanField(default=True)
    def __str__(self):
        return self.Part_code


class Feasibility_Detail(models.Model):
    Feasibility_id = models.CharField(max_length=30, primary_key=True,default = 'None')
    Product_detail = models.ForeignKey(Product_Detail,on_delete=models.CASCADE,default=None)
    Drawing_readability = models.CharField(max_length=10)
    Dimensional_tolerance = models.CharField(max_length=20)
    Cast_material = models.CharField(max_length=20)
    Hardness_required = models.CharField(max_length=20)
    Resource_requirement = models.CharField(max_length=20)
    Whether_all_dimensions_given = models.CharField(max_length=10)
    Type_of_mould = models.CharField(max_length=20)
    No_of_cavity = models.IntegerField()
    Core_type = models.CharField(max_length=20)
    Approx_core_weight = models.IntegerField(null =True)
    Core_box_detail = models.CharField(max_length=20,null=True)
    Reinforcement_in_core = models.CharField(max_length=20,null=True)
    Pattern_overall_size = models.CharField(max_length=30)
    Minimum_wall_thickness = models.CharField(max_length=30)
    Casting_weight = models.IntegerField()
    Casting_weight_per_box = models.IntegerField()#Formula used
    Approx_pouring_weight = models.CharField(max_length=30)
    Yield = models.IntegerField()#formula used
    Frame_requirement = models.CharField(max_length=30)
    Chill_requirement = models.CharField(max_length = 10)
    Pattern_material = models.CharField(max_length=30)
    Filter_requirement = models.CharField(max_length=10)
    Fettling_requirement = models.CharField(max_length=30)
    Pattern_core_box_cost = models.CharField(max_length=30)
    Casting_surface_coating = models.CharField(max_length=30)
    Match_plate_cost = models.CharField(max_length=30)
    Surface_treatment_cost = models.CharField(max_length=30)
    Development_cost = models.CharField(max_length=30)
    PPAP = models.CharField(max_length=30)
    Pattern_development_time = models.TextField()
    Bulk_lot_lead_time = models.CharField(max_length=20)
    Rejection_level_estimation = models. CharField(max_length=30)
    Head_treatment_requirement = models.CharField(max_length=10)
    Supplier_identification = models.CharField(max_length=30)
    Heat_no_detail = models.CharField(max_length=30)
    Conclusion = models.CharField(max_length=15)
    Not_feasible_reason = models.TextField(null=True)
    Customer_special_requirement = models.TextField(null = True)
    BFC_constraints = models.TextField(null = True)
    Comments = models.TextField(null=True)
    Date = models.DateField(default = None,null=True)
    Time = models.TimeField(default = None,null=True)


