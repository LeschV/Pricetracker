from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import json
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Заглушки для парсеров
class AmazonParser:
    def search_product(self, product_name):
        return [{'title': f'{product_name} - Amazon', 'price': 29999, 'image_url': '', 'url': '', 'marketplace': 'amazon'}]

class WildberriesParser:
    def search_product(self, product_name):
        return [{'title': f'{product_name} - Wildberries', 'price': 28500, 'image_url': '', 'url': '', 'marketplace': 'wildberries'}]

class SeasonalAnalyzer:
    def predict_best_purchase_time(self, product_name, category):
        return {'best_month': 11, 'months_to_wait': 2, 'expected_discount': 15, 'recommendation': 'Лучшее время - ноябрь'}

# Базовые функции
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'pages/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'pages/login-form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def login_choice(request):
    return render(request, 'pages/login.html')

@login_required
def account_dashboard(request):
    return render(request, 'pages/account.html', {'user': request.user})

def product_search(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name', '')
        if product_name:
            amazon_results = AmazonParser().search_product(product_name)
            wb_results = WildberriesParser().search_product(product_name)
            seasonal_advice = SeasonalAnalyzer().predict_best_purchase_time(product_name, 'electronics')
            context = {
                'search_query': product_name,
                'results': amazon_results + wb_results,
                'seasonal_advice': seasonal_advice,
                'results_count': 2
            }
            return render(request, 'pages/search_results.html', context)
    return render(request, 'pages/product_search.html')