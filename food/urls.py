from django.contrib import admin
from django.urls import path
from .views import index, items, detail, create_item, update_item,delete_item

app_name = 'food'

urlpatterns = [
    
    path('', index, name='index'),
    path('<int:item_id>/', detail, name='detail'),
    path('items', items, name='items'),
    #add items
    path('add',create_item, name='create_item'),
    #edit
    path('update/<int:id>/',update_item, name='update_item'),
    path('delete/<int:id>/',delete_item, name='delete_item'),


]