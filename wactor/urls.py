from django.conf.urls import patterns, include, url
from django.contrib import admin
from wactor import settings
from wactor import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'wactor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.main_pg),
]
