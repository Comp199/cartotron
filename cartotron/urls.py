"""cartotron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from shop import views as shop_views

urlpatterns = [
    url(r'^$', shop_views.category_list, name="index"),
    url(r'^cart/$', shop_views.cart_contents, name="cart"),
    url(r'^cart/add/(?P<product_id>\d+)/$', shop_views.cart_add, name="cart_add"),
    url(r'^cart/remove/(?P<product_id>\d+)/$', shop_views.cart_remove, name="cart_remove"),
    url(r'^search/$', shop_views.search, name="search"),

    url(r'^categories/(?P<category_id>\d+)/$', shop_views.category_detail, name="category_detail"),
    url(r'^products/$', shop_views.product_list, name="product_list"),
    url(r'^products/(?P<product_id>\d+)/$', shop_views.product_detail, name="product_detail"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
