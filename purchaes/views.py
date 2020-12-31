from django.shortcuts import render
from .serializers import  Supplier_Detail_Serialize,Individual_Detail_Serialize
from .models import Supplier_Detail,Individual_Detail
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework.status import  HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.utils.timezone import now
# Create your views here.

class Supplier_Detail_View(ModelViewSet):
    serializer_class = Supplier_Detail_Serialize

    def get_queryset(self):
        query = Supplier_Detail.objects.all()
        return query
    def create(self, request, *args, **kwargs):
        query = request.data
        print(query)
        try:
            query_object = Supplier_Detail.objects.create(Supplier_id=query['Supplier_id'],Supplier_name = query['Supplier_name'],
                                                          Address = query['Address'], Contact = query['Contact'],
                                                          Email_id = query['Email_id'], Nature_of_business = query['Nature_of_business'], 
                                                          Sales_tax_register_number= query['Sales_tax_register_number'],Distributor_stockist_for=query['Distributor_stockist_for'],List_of_items_handled=query['List_of_items_handled'],
                                                          Details_of_presnt_reputed_customers=query['Details_of_presnt_reputed_customers'],
                                                          Facilities_instruments_available=query['Facilities_instruments_available'],
                                                          Equipments=query['Equipments'],
                                                          Instruments=query['Instruments'],
                                                          Any_other_information=query['Any_other_information'],



                                                          Date = now().strftime("%Y-%m-%d"),
                                                          Time = now().strftime("%H:%M:%S")
                                                      )
            query_object.save()
            return Response("Succesfully Done!!!",status=HTTP_200_OK)

        except Exception as e:
            return Response(e,status=HTTP_400_BAD_REQUEST)



class Individual_Detail_View(ModelViewSet):
    serializer_class = Individual_Detail_Serialize

    def get_queryset(self):
        query = Individual_Detail.objects.all()
        return query
    def create(self, request, *args, **kwargs):
        query = request.data
        print(query)
        try:
            query_object = Individual_Detail.objects.create(Supplier_detail  = Supplier_Detail.objects.get(Supplier_id = query['Supplier_detail' ]),
                                                     Name= query['Name'], Designation = query['Designation'],
                                                            Email_id = query['Email_id'],Contact = query['Contact'],
                                                      Date = now().strftime("%Y-%m-%d"),
                                                      Time = now().strftime("%H:%M:%S") )
            query_object.save()
            return Response("Succesfully Done!!!",status=HTTP_200_OK)

        except:
            return  Response("Unable to Done!!!", status= HTTP_400_BAD_REQUEST )
