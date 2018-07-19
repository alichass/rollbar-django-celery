from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'rbexample.views.home', name='home'),
    url(r'^broken$', 'rbexample.views.broken', name='broken'),
    url(r'^delay$', 'rbexample.views.delay_broken', name='delay'),
    url(r'^delaysub$', 'rbexample.views.delay_ok', name='delaysub'),
    url(r'^admin/', include(admin.site.urls)),
]
