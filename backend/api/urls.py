from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
]
#STEP14 Go to urls.py from backend app and link such that this is the main urls.py
#Note: if your terminal doesnt allow you to write press CTRL + C
