from django.urls import path

from . import views
urlpatterns = [
    path('menu_item_api/', views.MenuItemAPI.as_view(), name='menu_item_api'),
    path('menu_item_api/<int:id>/', views.MenuItemAPI.as_view(), name='menu_item_api'),

]
