from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SingUp.as_view(), name='signup'),
    path('mypage/', views.userinfo, name='mypage'),
]
