# Dosya Adı: src/core/urls.py
from django.contrib import admin
from django.urls import path, include # 'include'u import ettiğinden emin ol
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Login URL'i
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    # Bizim yazdığımız Register endpoint'inin yolu
    path('api/auth/', include('auth.urls')),
]