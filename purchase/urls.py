from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from .views import  Supplier_Detail_View,Supplier_assessment_view,Supplier_evaluation_view,Supplier_rating_view
router = DefaultRouter()

router.register('Supplier_Detail', Supplier_Detail_View,basename='Supplier_Detail')
router.register('Supplier_Assessment', Supplier_assessment_view,basename='Supplier_Assessment')
router.register('Supplier_Evaluation', Supplier_evaluation_view,basename='Supplier_Evaluation')
router.register('Supplier_Rating', Supplier_rating_view,basename='Supplier_Rating')


urlpatterns = [url('/',include(router.urls))]