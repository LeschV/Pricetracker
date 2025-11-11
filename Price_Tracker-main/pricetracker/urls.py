from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('login-form/', TemplateView.as_view(template_name='login-form.html'), name='login_form'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('products/', TemplateView.as_view(template_name='products.html'), name='products'),
    path('account/', TemplateView.as_view(template_name='account.html'), name='account'),
]