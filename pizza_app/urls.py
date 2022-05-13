from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user.urls', namespace='user')),
    path('', include('pizza.urls', namespace='pizza')),
    path('order/', include('order.urls', namespace='order')),
    path('cart/', include('cart.urls', namespace='cart'))
]

