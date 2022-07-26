from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.main, name='main_url'),
    path('', views.store, name='store_url'), 
    path('cart/', views.cart, name='carts_url'),   
    path('checkout/', views.checkout, name='checkout_url'), 
    
    path('update_item/', views.updateItem, name='update_item'), 
    path('process_order/', views.processOrder, name='process_order'),   
         
]
