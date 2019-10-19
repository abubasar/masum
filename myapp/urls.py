from django.conf.urls import url 
from myapp import views 
 
urlpatterns = [ 
    url(r'^customers/$', views.customer_list),
    url(r'^customers/pk=1/$', views.customer_detail),
   # url(r'^customers/age/(?P&lt;age&gt;[0-9]+)/$', views.customer_list_age),
]