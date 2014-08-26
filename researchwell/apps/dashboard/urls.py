from django.views.generic import RedirectView
from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

import views

urlpatterns = patterns('',

    # Landing page
    url(r'^[/]?$', \
        views.home, \
        name='home'),

)
