from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .serializers import  Supplier_Detail_Serialize,Supplier_Evaluation_Serialize,Supplier_rating_Serialize
from .models import Supplier_Detail
from rest_framework.viewsets import  ModelViewSet
from rest_framework.response import Response
from rest_framework.status import  HTTP_200_OK,HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from django.utils.timezone import now


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
                                                          GST_no = query['GST_no'],
                                                          Email_id = query['Email_id'], Nature_of_business = query['Nature_of_business'],
                                                          Distributor=query['Distributor'],List_of_item=query['List_of_item'],
                                                          Details=query['Details'],
                                                          Facilities=query['Facilities'],
                                                          Information=query['Information'],
                                                          Date = now().strftime("%Y-%m-%d"),
                                                          Time = now().strftime("%H:%M:%S")
                                                      )
            query_object.save()
            return Response("Succesfully Done!!!",status=HTTP_200_OK)

        except Exception as e:
            return Response(e,status=HTTP_400_BAD_REQUEST)

