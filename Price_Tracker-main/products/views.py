from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """Главная страница Price Tracker"""
    context = {
        'title': 'Price Tracker - Отслеживание цен',
        'features': [
            'Отслеживание цен на товары',
            'Анализ факторов влияния на цену',
            'Умные уведомления',
            'Рекомендации по покупке'
        ]
    }
    return render(request, 'home.html', context)

def product_list(request):
    """Страница со списком товаров"""
    products = [
        {'name': 'Ноутбук ASUS', 'price': 75000, 'url': '#'},
        {'name': 'iPhone 15', 'price': 89990, 'url': '#'},
        {'name': 'Кроссовки Nike', 'price': 5990, 'url': '#'},
    ]
    return render(request, 'products/list.html', {'products': products})

def product_detail(request, product_id):
    """Страница товара"""
    return HttpResponse(f"Страница товара {product_id}")

def account_dashboard(request):
    """Страница личного кабинета"""
    tracked_products = [
        {'name': 'iPhone 15', 'price': 89990},
        {'name': 'Ноутбук ASUS', 'price': 75000},
        {'name': 'Кроссовки Nike', 'price': 5990},
    ]
    return render(request, 'account/dashboard.html', {
        'tracked_products': tracked_products
    })
def login_page(request):
    return render(request, 'login.html')

def login_form(request):
    return render(request, 'login-form.html')

def register_page(request):
    return render(request, 'register.html')