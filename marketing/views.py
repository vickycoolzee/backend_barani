from django.shortcuts import render
from .serializers import  Customer_Detail_Serialize,Order_Detail_Serialize,Individual_Detail_Serialize
from .models import Customer_Detail,Order_Detail,Individual_Detail
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework.status import  HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.utils.timezone import now
# Create your views here.

class Customer_Detail_View(ModelViewSet):
    serializer_class = Customer_Detail_Serialize

    def get_queryset(self):
        query = Customer_Detail.objects.all()
        return query
    def retrieve(self, request, *args, **kwargs):
        params =kwargs
        print(params)
        try:
            query = Customer_Detail.objects.get(Customer_id = params['pk'])
            query_serialize = Customer_Detail_Serialize(query)
            return Response(query_serialize.data, status=  HTTP_200_OK)
        except:
            return  Response(" Failure ",status= HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        query = request.data
        print(query)
        try:
            query_object = Customer_Detail.objects.create(Customer_id=query['Customer_id'],Customer_name = query['Customer_name'],
                                                          Nick_name = query['Nick_name'], Address = query['Address'],
                                                          GST_no = query['GST_no'], CIN_no = query['CIN_no'], Date = now().strftime("%Y-%m-%d"),
                                                          Time = now().strftime("%H:%M:%S")
                                                      )
            query_object.save()
            return Response("Succesfully Done!!!",status=HTTP_200_OK)

        except Exception as e:
            return Response(e,status=HTTP_400_BAD_REQUEST)

class Order_Detail_View(ModelViewSet):
    serializer_class = Order_Detail_Serialize

    def get_queryset(self):
        query = Order_Detail.objects.all()
        return query
    def retrieve(self, request, *args, **kwargs):
        params =kwargs
        print(params)
        try:
            query = Order_Detail.objects.get(Customer_id = Customer_Detail.objects.get(Customer_id = params['pk']))
            query_serialize = Order_Detail_Serialize(query)
            return Response(query_serialize.data, status=  HTTP_200_OK)
        except:
            return  Response(" Failure ",status= HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        query = request.data
        print(query)
        try:
            query_object = Order_Detail.objects.create(Customer_id = Customer_Detail.objects.get(Customer_id = query['Customer_id']) ,Ventor_code=query['Ventor_code'], Part_code = query['Part_code'],
                                                      Part_name = query['Part_name'],Casting_type = query['Casting_type'], Pattern_scope = query['Pattern_scope'],
                                                      Transport = query['Transport'], Painting_method = query['Painting_method'],
                                                      Packing_type = query['Packing_type'],Machinary_type = query['Machinary_type'],
                                                      Payment_terms = query['Payment_terms'],Export_required = query['Export_required'],
                                                      Quantity = query['Quantity'],Payments_terms_days = query['Payments_terms_days'], Date = now().strftime("%Y-%m-%d")
                                                      ,Time = now().strftime("%H:%M:%S") )
            query_object.save()
            return Response("Succesfully Done!!!",status=HTTP_200_OK)

        except:
            return  Response("Unable to Done!!!", status= HTTP_400_BAD_REQUEST )




class Individual_Detail_View(ModelViewSet):
    serializer_class = Individual_Detail_Serialize

    def get_queryset(self):
        query = Individual_Detail.objects.all()
        return query
    def retrieve(self, request, *args, **kwargs):
        params =kwargs
        print(params)
        try:
            query = Individual_Detail.objects.get(Customer_id = Customer_Detail.objects.get(Customer_id = params['pk']))
            query_serialize = Individual_Detail_Serialize(query)
            return Response(query_serialize.data, status=  HTTP_200_OK)
        except:
            return  Response(" Failure ",status= HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        query = request.data
        print(query)
        try:
            query_object = Individual_Detail.objects.create(Customer_id = Customer_Detail.objects.get(Customer_id = query['Customer_id']),
                                                     Name= query['Name'], Designation = query['Designation'],
                                                            Email_id = query['Email_id'],Contact = query['Contact'],
                                                      Date = now().strftime("%Y-%m-%d"),
                                                      Time = now().strftime("%H:%M:%S") )
            query_object.save()
            return Response("Succesfully Done!!!",status=HTTP_200_OK)

        except:
            return  Response("Unable to Done!!!", status= HTTP_400_BAD_REQUEST )


