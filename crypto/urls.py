from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemap import *
from .views import *
app_name= 'crypto'

sitemaps = {
 'pages': PageSitemap,
}
urlpatterns = [
    path('', home_page, name= 'home_page'),
    path('prices', prices, name= 'prices'),
    path('news', news, name= 'news'),
    path('all_prices', all_price, name= 'all_price'),
    path('daily_pair', daily_Pair, name= 'daily'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    
]