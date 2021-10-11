
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^staff$', views.staff, name='staff'),
    url(r'^staff/detail/(?P<pk>\d+)$', views.staff_detail, name='staff-detail'),
    url(r'^product$', views.product, name='product'),
    url(r'^product/delete/(?P<pk>\d+)$', views.product_delete, name='product-delete'),
    url(r'^product/update/(?P<pk>\d+)$', views.product_update, name='product-update'),
    url(r'^order$', views.order, name='order'),
]
