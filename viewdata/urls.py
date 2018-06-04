from django.conf.urls import url
from . import views

app_name= 'viewdata'

urlpatterns = [
    url(r'^$', views.type_list, name='type_list'),
    url(r'^drinks/$', views.drink_list, name='drink_list'),
    url(r'^chocolate/$', views.chocolate_list, name='chocolate_list'),
    url(r'^chips/$', views.chips_list, name='chips_list'),
    url(r'^biscuits/$', views.biscuit_list, name='biscuit_list'),
    url(r'^other/$', views.other_list, name='other_list'),
]
