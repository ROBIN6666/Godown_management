from django.conf.urls import url
from .views import *
from django.urls import path, include

urlpatterns= [
     url(r'^$',index,name='index'),
     url(r'^display_laptops$',display_Laptops,name='display_Laptops'),
     url(r'^display_dektops$',display_Desktops,name='display_Desktops'),
     url(r'^display_mobiles$',display_Mobiles,name='display_Mobiles'),
    
    
     url(r'^add_Laptops$',add_Laptops,name='add_Laptops'),
     url(r'^add_desktop$',add_Desktop,name='add_Desktop'),
     url(r'^add_mobile$',add_Mobiles,name='add_Mobiles'),

     url(r'laptops/edit_device/(?P<pk>\d+)$',edit_laptop,name='edit_laptop'),
     url(r'^desktops/edit_device/(?P<pk>\d+)$',edit_desktop,name='edit_desktop'),
     url(r'^mobile/edit_device/(?P<pk>\d+)$',edit_mobile,name='edit_mobile'),

     url(r'^laptop/delete_device/(?P<pk>\d+)$',delete_laptop,name='delete_laptop'),
     url(r'^desktops/delete_device/(?P<pk>\d+)$',delete_desktop,name='delete_desktop'),
     url(r'^mobile/delete_device/(?P<pk>\d+)$',delete_mobile,name='delete_mobile'),

     

]