"""account URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import SignUpAPI, SignInAPI, LabelAPI

app_name = 'account'

urlpatterns = [
    path('signup', SignUpAPI.as_view()),
    path('signin', SignInAPI.as_view()),
    path('label', LabelAPI.as_view()),
    path('label/<int:account_id>', LabelAPI.as_view()),
]
