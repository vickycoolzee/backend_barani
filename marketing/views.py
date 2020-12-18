from django.shortcuts import render
from .serializers import  Customer_Detail_Serialize
from .models import Customer_Detail
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework.status import  HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
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
            query_object = Customer_Detail.objects.create(Customer_id=query['Customer_id'], Email_id = query['Email_id'],
                                                      Customer_name = query['Customer_name'],Nick_name = query['Nick_name'], Address = query['Address'],
                                                      GST_no = query['GST_no'], CIN_no = query['CIN_no'],
                                                      Contact_1 = query['Contact_1'],Contact_2 = query['Contact_2'],
                                                      Contact_3 = query['Contact_3'],Contact_4 = query['Contact_4']
                                                      )
            query_object.save()
            return Response("Succesfully Done!!!",status=HTTP_200_OK)

        except:
            return  Response("Unable to Done!!!", status= HTTP_400_BAD_REQUEST )

