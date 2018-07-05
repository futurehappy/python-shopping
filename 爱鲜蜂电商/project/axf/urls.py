# -*- coding:utf-8 -*-

from django.conf.urls import url
from axf import views

urlpatterns = [
    url(r'home/$',views.home),
    url(r'market/(\w+)/(\w+)/(\w+)/$',views.market),
    url(r'^cart/$',views.cart),
    #修改购物车  增加、减少
    url(r'^changecart/(\d+)/$', views.changecart),
    # 修改购物车  是否选中
    url(r'^changecart2/$', views.changecart2),
    # 下订单
    url(r'^qOrder/$', views.qOrder),

    url(r'mine/$',views.mine),
    #登陆界面
    url(r'login/$', views.login),
    url(r'quit/$', views.quit),
    url(r'addresses/$', views.addresses),
    url(r'addaddress/$', views.addaddress),
]