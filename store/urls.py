from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-product/', views.add_product, name='add_product'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    # Authentication URLs
    path('user/login/', auth_views.LoginView.as_view(template_name='store/login.html'), name='login'),
    path('user/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
