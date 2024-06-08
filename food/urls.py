from django.contrib import admin
from django.urls import path
from .views import index, items, detail

app_name = 'food'

urlpatterns = [
    
    path('', index, name='index'),
    path('<int:item_id>/', detail, name='detail'),
    path('items', items, name='items'),

]