from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import Customer_Detail_View,Order_Detail_View,Individual_Detail_View,Product_Detail_View,Feasibility_Detail_View
router = DefaultRouter()
router.register('Customer_Detail', Customer_Detail_View,basename='Customer_Detail')
router.register('Order_Detail',Order_Detail_View,basename='Order_Detail')
router.register('Individual_Detail',Individual_Detail_View,basename='Individual_Detail')
router.register('Product_Detail_View',Product_Detail_View,basename='Product_Detail_View')
router.register('Feasibility_Detail_View',Feasibility_Detail_View,basename='Feasibility_Detail_View')

urlpatterns = [
    url('/',include(router.urls))

]