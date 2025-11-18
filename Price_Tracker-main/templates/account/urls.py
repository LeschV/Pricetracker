from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login-form/', views.login_view, name='login_form'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.account_dashboard, name='account_dashboard'),
    path('search/', views.product_search, name='product_search'),
    path('track-product/', views.track_product, name='track_product'),
]