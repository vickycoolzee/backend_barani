from django.contrib import admin
from django.urls import path,include
from marketing import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('marketing',include("marketing.urls")),
    path('purchase',include("purchase.urls")),
    path('testing',views.test)
]
