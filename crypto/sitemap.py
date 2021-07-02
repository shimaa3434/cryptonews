from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class PageSitemap(Sitemap):
    changefreq = 'monthly'
    def items(self):
        page = ['crypto:home_page', 'crypto:prices', 'crypto:news', 'crypto:all_price', ]
        return page
    
    def location(self, itme):
        return reverse(itme)