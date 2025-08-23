# Dosya Adı: src/auth/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

class AuthTests(APITestCase):
    def setUp(self):
        # Testler için gerekli URL'leri burada tanımlayalım
        # DİKKAT: 'auth/urls.py' dosyasındaki name='register'dan geliyor
        self.register_url = reverse('register') 
        # DİKKAT: Ana 'core/urls.py' dosyasındaki name='login'dan geliyor
        self.login_url = reverse('login') 

    def test_register_user_success(self):
        """Yeni bir kullanıcının başarıyla kaydolabildiğini test eder."""
        data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpassword123"
        }
        response = self.client.post(self.register_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_login_user_success(self):
        """Mevcut bir kullanıcının başarıyla giriş yapabildiğini test eder."""
        # Önce bir kullanıcı oluşturalım
        User.objects.create_user(username='loginuser', password='loginpassword123')
        data = {
            "username": "loginuser",
            "password": "loginpassword123"
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response.data)
