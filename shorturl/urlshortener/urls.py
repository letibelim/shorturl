from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'shorturl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.urlform, name= 'form'),
    url(r'^(?P<code>\w+)/$', views.redirection, name='redirection'),
    url(r'allurl$', views.all_redirections, name='allurl'),
    url(r'^test$', views.test, name = 'test'),
    

]