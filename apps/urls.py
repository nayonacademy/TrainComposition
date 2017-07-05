from django.conf.urls import url

from apps import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
]