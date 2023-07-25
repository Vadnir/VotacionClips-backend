from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from .views import UserView

"""
urls for the user api
"""
urlpatterns = [
    path("", UserView.as_view()),
    path('auth/', views.obtain_auth_token),
]
