# Dosya Adı: src/auth/serializers.py

from rest_framework import serializers
from .models import CustomUser  # Kendi yazdığımız CustomUser modelini import ediyoruz

class RegisterSerializer(serializers.ModelSerializer):
    """
    Yeni bir kullanıcı kaydı oluşturmak için kullanılan serializer.
    Gelen veriyi doğrular ve yeni bir CustomUser nesnesi yaratır.
    """
    class Meta:
        model = CustomUser  # Artık standart User yerine CustomUser modelini kullanıyoruz
        
        # API'dan kabul edeceğimiz ve API'dan geri döndüreceğimiz alanlar
        fields = ('id', 'username', 'email', 'password')
        
        # 'password' alanı için özel ayarlar
        extra_kwargs = {
            'password': {
                'write_only': True, # Bu, şifrenin API cevabında asla geri gönderilmemesini sağlar (Güvenlik!)
                'style': {'input_type': 'password'} # DRF'in arayüzünde şifre alanı olarak görünmesini sağlar
            }
        }

    def create(self, validated_data):
        """
        Doğrulanmış veriyi kullanarak yeni bir kullanıcı oluşturur.
        create_user metodu, şifrenin düz metin olarak değil,
        şifrelenmiş (hashed) bir şekilde veritabanına kaydedilmesini sağlar.
        """
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user