from django.conf.urls import url
from matjar import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]