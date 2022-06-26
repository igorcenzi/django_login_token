from rest_framework import serializers

from users.models import User

class UserSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  email = serializers.EmailField()
  password = serializers.CharField(max_length=100 ,write_only=True)
  
  def validate_email(self, value):
    if User.objects.filter(email__iexact=value).exists():
      raise serializers.ValidationError('Email already exists.')
    
    return value
  
  def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user