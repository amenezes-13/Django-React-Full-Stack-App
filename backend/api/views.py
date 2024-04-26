from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .Serializers import UserSerializer, NoteSerializer # add the NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# Add the new code after Step 11
from .models import Note
#step12: create a new class
class NoteListCreate(generics.ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

# After this we go to STEP 13: go to API folder and create a new file called urls.py
# this is not to be mixed with urls.py from backend App

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# This is done for now.
# Head over to the BACKEND APP created (NOT THE MAIN FOLDER) where you have the --init-- (NOT THE MIGRATIONS)
# AND CHOOSE urls.py