from rest_framework import serializers
from .models import auth

class authSerializer(serializers.ModelSerializer) :
    eamilAddress = serializers.CharField()
    authCode = serializers.CharField()
    verified = serializers.BooleanField()
    lastModifiedAt = serializers.DateTimeField()

    class Meta:
        model = auth
        fields = ['eamilAddress', 'authCode', 'verified', 'lastModifiedAt']
