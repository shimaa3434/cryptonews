from django.shortcuts import render
import requests
import json

# Create your views here.
def home_page(request):
    api_news= requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api= json.loads(api_news.content)
    
    api_price= requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,BNB,ADA,DOGE,XRP,USDC,DOT,UNI&tsyms=USD')
    price= json.loads(api_price.content)
    
    context= {'api': api, 'price': price}
    return render(request, 'crypto/home_page.html', context )

def prices(request):
    if request.method == 'POST':
        q= request.POST['q']
        q= q.upper()
        q_price= requests.get(f'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={q}&tsyms=USD')
        q_data= json.loads(q_price.content)
        return render(request,'crypto/prices_page.html', {'q': q, 'q_data': q_data})
    else:
        no= 'رسالة بان العملة غير موجودة من الاساس'
        return render(request, 'crypto/prices_page.html', {'no': no} )


def news(request):
    api_news= requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api= json.loads(api_news.content)
    context= { 'api': api}
    return render(request, 'crypto/news_page.html', context)

def all_price(request):
    api_price= requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,USDT,BNB,ADA,DOGE,XRP,USDC,DOT,UNI&tsyms=USD')
    price= json.loads(api_price.content)
    context= {'price': price}
    return render(request, 'crypto/all_price_page.html', context)

def daily_Pair (request):
    labels= []
    datas= []
    api_daily= requests.get('https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=20')
    daily= json.loads(api_daily.content)
    context= {
        'daily': daily,
    }
    return render(request, 'crypto/daily_pair.html', context)