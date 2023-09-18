from django.urls import path
from .import views

urlpatterns = [
    path('UserRegisterapi',views.UserRegisterapi.as_view(),name='UserRegisterapi'),
    path('UserLoginpage',views.UserLoginpage.as_view(),name='UserLoginpage'),
]
