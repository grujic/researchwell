from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'researchwell.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    ### User facing stuff ###
    url(r'',
        include('researchwell.apps.dashboard.urls',
        namespace='dashboard')),

    url(r'^admin/', include(admin.site.urls)),
)
