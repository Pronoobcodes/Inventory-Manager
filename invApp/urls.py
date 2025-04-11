from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.product_create_view, name='product-create'),
    path('productlist/', views.product_list_view, name='product-list'),
    path('productdelete/<int:pk>', views.product_update_view, name='product-update'),
    path('productupdate/<int:pk>', views.product_delete_view, name='product-delete'),
]