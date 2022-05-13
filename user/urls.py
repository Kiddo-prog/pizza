from django.urls import path
from . import views as user_view

app_name='user'
urlpatterns = [
    path('register/', user_view.register, name='register'),
    path('login/', user_view.LoginUser.as_view(), name='login'),
    path('logout/', user_view.LogoutUser.as_view(), name='logout')
]