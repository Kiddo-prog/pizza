from django.urls import path
from . import views as pizza_view

app_name='pizza'
urlpatterns = [path('', pizza_view.dashboard, name='dashboard'), path('list/', pizza_view.ListPizza.as_view(), name='list'), path('detail/<slug>/', pizza_view.pizza_detail, name='detail')]