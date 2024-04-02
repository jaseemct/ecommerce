from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('user_home',views.user_home,name='user_home'),
    path('signup1',views.signup1,name='signup1'),
    path('signup',views.signup,name='signup'),
    path('login1',views.login1,name='login1'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('add_catagorypage',views.add_catagorypage,name='add_catagorypage'),
    path('add_catagory',views.add_catagory,name='add_catagory'),
    path('add_productpage',views.add_productpage,name='add_productpage'),
    path('add_product',views.add_product,name='add_product'),
    path('view_product',views.view_product,name='view_product'),
    path('view_user',views.view_user,name='view_user'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('delete_user/<int:tid>',views.delete_user,name='delete_user'),
    path('products_page',views.products_page,name='products_page'),
    path('products_by_catagory',views.products_by_catagory,name='products_by_catagory'),
    path('cart',views.cart,name='cart'),
    path('cart_details/<int:id>',views.cart_details,name='cart_details'),
    path('decrease_quantity/<int:id>/', views.decrease_quantity, name='decrease_quantity'),
    path('increase_quantity/<int:id>/', views.increase_quantity, name='increase_quantity'),
    path('remove_cart/<int:id>',views.remove_cart,name='remove_cart'),
    path('navbar2',views.navbar2,name='navbar2'),
    path('logout',views.logout,name='logout'),
]