from django.shortcuts import render

def index(request):
    return render(request, 'notifications/index.html')

def price_alerts(request):
    return render(request, 'notifications/alerts.html')