from django.conf.urls import url
from dashboard.category import views

urlpatterns = [
    url(r'^$', views.CategoryList.as_view(), name='category_list'),
    url(r'^create/$', views.CategoryCreate.as_view(), name='category_create'),
]