from django.shortcuts import render

def product_list(request):
    # Временные данные для демонстрации
    products = [
        {
            'name': 'Смартфон iPhone 15 Pro 256GB',
            'price': '89 990',
            'marketplace': 'Wildberries',
            'trend': 'down',
            'discount': '15%'
        },
        {
            'name': 'Ноутбук ASUS VivoBook 15',
            'price': '54 990', 
            'marketplace': 'OZON',
            'trend': 'stable',
            'discount': '8%'
        },
    ]
    # Используем ваш готовый шаблон products/list.html
    return render(request, 'products/list.html', {'products': products})

def product_search(request):
    # Используем ваш готовый шаблон
    return render(request, 'pages/product_search.html')

def search_results(request):
    # Используем ваш готовый шаблон
    return render(request, 'pages/search_results.html')

def home_view(request):
    # Используем ваш готовый шаблон главной страницы
    return render(request, 'pages/home.html')