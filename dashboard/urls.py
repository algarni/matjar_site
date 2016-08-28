from django.conf.urls import url, include
from dashboard import views
from .product.urls import urlpatterns as product_urls
from .category.urls import urlpatterns as category_urls

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/', include(product_urls)),
    url(r'^category/', include(category_urls)),
]