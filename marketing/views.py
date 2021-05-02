from django.shortcuts import render
from django.utils.timezone import datetime

from .serializers import  Customer_Detail_Serialize,Order_Detail_Serialize,Individual_Detail_Serialize,Product_Detail_Serialize,Feasibility_Detail_Serialize
from .models import Customer_Detail,Order_Detail,Individual_Detail,Product_Detail,Feasibility_Detail
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework.status import  HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.utils.timezone import now
# Create your views here.

def test(request):
    data = str(datetime.now()).replace(':','')[-1:-7:-1]

    return render(request,"index.html",{'value':data})


class Customer_Detail_View(ModelViewSet):
    serializer_class = Customer_Detail_Serialize

    def get_queryset(self):
        query = Customer_Detail.objects.all()
        return query
    def create(self, request, *args, **kwargs):
        query = request.data
        print(query, now().strftime("%d-%m-%Y,%H:%M"))
        try:
            query_object = Customer_Detail.objects.create(Customer_id=query['Customer_id'],Customer_name = query['Customer_name'],
                                                          Nick_name = query['Nick_name'], Address = query['Address'],
                                                            Email_id = query['Email_id'],
                                                          GST_no = query['GST_no'], CIN_no = query['CIN_no'], Datime = now().strftime("%d-%m-%Y_%I:%M:%S:%p")
                                                      )
            query_object.save()
            return Response("Succesfully Done!!!",status=HTTP_200_OK)

        except Exception as e:
            return Response(e,status=HTTP_400_BAD_REQUEST)



class Individual_Detail_View(ModelViewSet):
    serializer_class = Individual_Detail_Serialize

    def get_queryset(self):
        data= self.request.query_params.get('id')
        query = Individual_Detail.objects.filter(Customer_detail = data)
        print(query)
        return query
    
    def create(self, request, *args, **kwargs):
        query1 = request.data
        try:
            for query in query1:
                query_object = Individual_Detail.objects.create(Customer_detail  = Customer_Detail.objects.get(Customer_id = query['Customer_id']),
                                                     Name= query['Name'], Designation = query['Designation'],
                                                            Email_id = query['Email_id'],Contact = query['Contact'],
                                                      Datime = now().strftime("%d-%m-%Y_%I:%M:%S:%p") )
                query_object.save()
            return Response("Succesfully Done!!!",status=HTTP_200_OK)

        except Exception as e:
            print("Error",e)
            return  Response("Unable to Done!!!", status= HTTP_400_BAD_REQUEST )





class Order_Detail_View(ModelViewSet):
    serializer_class = Order_Detail_Serialize

    def get_queryset(self):
        query = Order_Detail.objects.all()
        return query

    def create(self, request, *args, **kwargs):
        query = request.data
        print(query)
        try:
            query_object = Order_Detail.objects.create(Customer_detail = Customer_Detail.objects.get(Customer_id = query['Customer_detail']) ,RFQ_id = query['RFQ_id'], Datime = now().strftime("%d-%m-%Y_%I:%M:%S:%p"))
            query_object.save()
            return Response("Succesfully Done!!!",status=HTTP_200_OK)

        except:
            return  Response("Unable to Done!!!", status= HTTP_400_BAD_REQUEST )



class Product_Detail_View(ModelViewSet):
    serializer_class = Product_Detail_Serialize

    def get_queryset(self):
        data= self.request.query_params.get('id')
        print("data",data)
        if data is not None:
            print(data,Order_Detail.objects.get(RFQ_id = data))
            query = Product_Detail.objects.filter(RFQ_detail = Order_Detail.objects.get(RFQ_id = data))
            print(query)
            return query
        else:
            query = Product_Detail.objects.all()
            return query

    def create(self, request, *args, **kwargs):
        for query in request.data:
            try:
                print(query)
                query_object = Product_Detail.objects.create(
                        Product_id = query["Product_id"],
                        RFQ_detail=Order_Detail.objects.get(RFQ_id=query['RFQ_detail']),
                        Ventor_code=query['Ventor_code'], Part_code=query['Part_code'],
                        Part_name=query['Part_name'], Casting_type=query['Casting_type'], Pattern_scope=query['Pattern_scope'],
                        Transport=query['Transport'], Painting_method=query['Painting_method'],
                        Packing_type=query['Packing_type'], Machinary_type=query['Machinary_type'],
                        Payment_terms=query['Payment_terms'], Export_required=query['Export_required'],
                        Quantity=query['Quantity'], Payments_terms_days=query['Payments_terms_days'],
                        Datime = now().strftime("%d-%m-%Y_%I:%M:%S:%p"))
                query_object.save()
            except Exception as e:
                print(e)
                return Response("Unable to Upload data")
        return Response("Succesfully Done!!!", status=HTTP_200_OK)


class Feasibility_Detail_View(ModelViewSet):
    serializer_class = Feasibility_Detail_Serialize

    def get_queryset(self):
        query = Feasibility_Detail.objects.all()
        return query

    def create(self, request, *args, **kwargs):
        query = request.data
        print(query)
        query_object = Feasibility_Detail.objects.create(
        Product_detail=Product_Detail.objects.get(Product_id=query['Product_detail']),
        Drawing_readability=query['Drawing_readability'], Dimensional_tolerance=query['Dimensional_tolerance'],
        Cast_material=query['Cast_material'],Hardness_required=query['Hardness_required'],
        Resource_requirement=query['Resource_requirement'],Whether_all_dimensions_given=query['Whether_all_dimensions_given'],
        Type_of_mould=query['Type_of_mould'], No_of_cavity=query['No_of_cavity'],Core_type = query['Core_type'],
        Approx_core_weight=query['Approx_core_weight'], Core_box_detail=query['Core_box_detail'],
        Reinforcement_in_core=query['Reinforcement_in_core'],Pattern_overall_size=query['Pattern_overall_size'],
        Minimum_wall_thickness=query['Minimum_wall_thickness'],
        Casting_weight=query['Casting_weight'], Casting_weight_per_box=query['Casting_weight_per_box'],
        Approx_pouring_weight=query['Approx_pouring_weight'], Yield=query['Yield'],
        Frame_requirement=query['Frame_requirement'], Pattern_material=query['Pattern_material'],
        Fettling_requirement=query['Fettling_requirement'],Chill_requirement =query['Chill_requirement'],
        Pattern_core_box_cost=query['Pattern_core_box_cost'],Filter_requirement = query['Filter_requirement'],
        Casting_surface_coating=query['Casting_surface_coating'],
        Match_plate_cost=query['Match_plate_cost'], Surface_treatment_cost=query['Surface_treatment_cost'],
        Development_cost=['Development_cost'],
        PPAP = query['PPAP'], Pattern_development_time=query['Pattern_development_time'],
        Bulk_lot_lead_time=query['Bulk_lot_lead_time'],
        Rejection_level_estimation=query['Rejection_level_estimation'],
        Head_treatment_requirement=query['Head_treatment_requirement'],
        Conclusion=query['Conclusion'],Heat_no_detail = query['Heat_no_detail'],
        Not_feasible_reason=query['Not_feasible_reason'],Supplier_identification = query['Supplier_identification'],
        Customer_special_requirement=query['Customer_special_requirement'],
        BFC_constraints=query['BFC_constraints'],Comments=query['Comments'],
       Datime = now().strftime("%d-%m-%Y_%I:%M:%S:%p"))
        query_object.save()
        return Response("Succesfully Done!!!", status=HTTP_200_OK)
