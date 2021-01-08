from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import  Supplier_Detail_View
router = DefaultRouter()

router.register('Supplier_Detail', Supplier_Detail_View,basename='Supplier_Detail')
urlpatterns = [url('/',include(router.urls))]