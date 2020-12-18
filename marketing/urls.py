from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import Customer_Detail_View
router = DefaultRouter()
router.register('Customer_Detail', Customer_Detail_View,basename='Customer_Detail')

urlpatterns = [
    url('/',include(router.urls))

]