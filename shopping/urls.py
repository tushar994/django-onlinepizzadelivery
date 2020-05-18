from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = "main_page"),
    path('add_to_cart/<int:item>',views.add_to_cart ,name = "add_to_cart"),
    path('order',views.Order, name = 'order'),
    path('delete/<int:item>',views.delete_object,name = 'delete')
]