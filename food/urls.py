from django.contrib import admin
from django.urls import path
from .views import items, create_item, update_item,delete_item,IndexClassView,FoodDetail,CreateItem

app_name = 'food'

urlpatterns = [
    
    path('', IndexClassView.as_view(), name='index'),
    # path('<int:item_id>/', detail, name='detail'),
    path('<int:pk>/', FoodDetail.as_view(), name='detail'),

    path('items', items, name='items'),
    #add items
    path('add',CreateItem.as_view(), name='create_item'),
    #edit
    path('update/<int:id>/',update_item, name='update_item'),
    path('delete/<int:id>/',delete_item, name='delete_item'),


]