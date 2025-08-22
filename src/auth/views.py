# Dosya Adı: src/auth/views.py

from rest_framework import generics
from .models import CustomUser  # DİKKAT: Artık kendi modelimizi import ediyoruz
from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    # Bu View'in hangi veritabanı tablosuyla çalışacağını belirtiyoruz
    queryset = CustomUser.objects.all()
    
    # Bu View'in hangi "Kalite Kontrol Formu"nu kullanacağını belirtiyoruz
    serializer_class = RegisterSerializer