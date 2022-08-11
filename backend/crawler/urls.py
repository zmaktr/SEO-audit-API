from django.urls import path
from crawler.views import OnpageCrawl

urlpatterns = [
     path('onpage_crawl/', OnpageCrawl.as_view(), name='onpage_crawl')
]
