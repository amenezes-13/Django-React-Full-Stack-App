"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # add the include function
#Write the line of code below:
from api.views import CreateUserView # which was created in the views.py
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls), #write the path below
    path("api/user/register/", CreateUserView.as_view(), name = "register"),
    path("api/token/", TokenObtainPairView.as_view(), name = "get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name = "refresh"),
    path("api/auth", include("rest_framework.urls")),
    #this is STEP 13 TO LINK
    path("api/", include("api.urls")),
]
#Step14: we want to make sure the code is working. This wraps up the BACKEND CODE!

# done for now here. Bring up the terminal and start making migrations in the database in 2 steps:
#[1] python manage.py makemigrations
#[2] python manage.py migrate
#[3] Run the application by doing: python manage.py runserver 7000
# This 7000 I found here https://www.youtube.com/watch?v=jaTT4iPfweg becuase python manage.runserver returned the error
#Error: "You dont have permission to access that port"

#[5] Mow get the http://127.0.0.1:7000/

#Step 8: Make a new model inside api --> model.py. So head over to models.py