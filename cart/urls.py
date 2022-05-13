from django.urls import path
from . import views as cart_view

app_name='cart'
urlpatterns = [path('', cart_view.cart_detail, name='detail'),
path('add/<int:pizza_id>/', cart_view.cart_add, name='cart_add'),
path('remove/<int:pizza_id>/', cart_view.cart_remove, name='cart_remove')]