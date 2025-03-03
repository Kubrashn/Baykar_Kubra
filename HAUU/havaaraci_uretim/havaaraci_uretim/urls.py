from django.contrib import admin
from django.urls import path, include
from users.views import *  
from main.views import *  
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import redirect


schema_view = get_schema_view(
   openapi.Info(
      title="İHA Kiralama API",
      default_version='v1',
      description="İHA parçaları, uçaklar ve takımlar için API dokümantasyonu",
      terms_of_service="https://www.yourcompany.com/terms/",
      contact=openapi.Contact(email="contact@yourcompany.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()

def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login, name='home'),  
    path('', include('main.urls')),  
    path('login/', Kullanici_login, name='login'),  
    path('logout/', Kullanici_logout, name='logout'),  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),  
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'), 
    path('uretim/', uretim_paneli, name='uretim_paneli'),  
]
