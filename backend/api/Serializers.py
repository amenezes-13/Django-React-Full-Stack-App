from django.contrib.auth.models import User
from rest_framework import serializers
# STEP9: New line to use after models.py
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

# This is now done for now...go to views.py which is 2 files below this!

# STEP 10: Create a new class to accomodate the new serialiser from models.py

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at","author"]
        extra_kwargs = {"author": {"read_only": True}}

#STEP 11: Go back to views and make some views to create and deleting a note