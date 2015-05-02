from django.conf.urls import include, url
from wactor import settings
from blog import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'pgtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^home/$', views.home),
]
