from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'textGears.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'textGears.views.home', name='home'),
    url(r'^essay/', 'textGears.views.essay', name='essay'),
    url(r'^admin/', include(admin.site.urls)),
]
