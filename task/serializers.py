from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed', 'priority', 'archived']
        
    
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password']
        
    def create(self, validated_data):
        user = User(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
            validated_data.pop('password')
        return super().update(instance, validated_data)