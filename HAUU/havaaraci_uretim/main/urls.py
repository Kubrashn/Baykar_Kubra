from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('uretim_paneli/', uretim_paneli, name="uretım_paneli"),
    path('get_parcalar/<int:ucak_id>/', get_parcalar, name="get_parcalar"),
    path('uretim_yap/<int:parca_id>/', uretim_yap, name="uretim_yap"),
]
