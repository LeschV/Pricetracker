from django.contrib import admin
from django.urls import path, include
from products import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_views.home_view, name='home'),
    path('products/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    
    # Прямые маршруты для удобства
    path('login/', include('accounts.urls')),
    path('register/', include('accounts.urls')),
]