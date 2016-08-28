from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProductList.as_view(), name='product_list'),
    url(r'^create/$', views.create, name='product_create'),
]