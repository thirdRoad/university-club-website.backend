# Dosya Adı: src/auth/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import CustomUser # DİKKAT: Artık kendi modelimizi import ediyoruz

class AuthTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register') 
        self.login_url = reverse('login') 

    def test_register_user_success(self):
        """Yeni bir CustomUser'ın başarıyla kaydolabildiğini test eder."""
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Veritabanında 1 tane CustomUser olduğunu doğrula
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().username,'testuser')