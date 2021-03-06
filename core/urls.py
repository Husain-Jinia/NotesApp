"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from user import views as user_views
from notes import views as notes_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # auth url
    path('register/',user_views.register, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    # notes url
    path('home/',notes_views.CreateNotes.as_view(), name='create-note'),
    path('',notes_views.displayView, name='display-note'),
    path('updatenote/<int:pk>',notes_views.UpdateNote.as_view(), name='update-note'),
    path('deletenote/<int:pk>',notes_views.DeleteNote.as_view(), name='delete-note'),
    path('pinnote/<int:id>',notes_views.pin, name='pin-note')  

]
